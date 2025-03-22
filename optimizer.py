from dotenv import load_dotenv
import os
from openai import OpenAI
import syllapy
import matplotlib.pyplot as plt
import pandas as pd

# readability metric calculation
def calculate_readability(text):
    # Calculate the average number of words per sentence
    words = text.split()
    sentences = text.split(".")
    num_words = len(words)
    num_sentences = len(sentences)
    avg_words_per_sentence = len(words) / len(sentences)
    
    # Calculate the average number of syllables per word
    syllables = 0
    for word in words:
        syllables += syllapy.count(word)
    avg_syllables_per_word = syllables / len(words)
    
    # Calculate the Flesch-Kincaid Grade Level
    flesch_kincaid = 0.39 * avg_words_per_sentence + 11.8 * avg_syllables_per_word - 15.59
    return [flesch_kincaid, num_words, num_sentences]

def save_statistics(text, response):
    # Calculate the readability of the original text
    results_original = calculate_readability(text)
    readability_original = results_original[0]
    num_words_original = results_original[1]
    num_sentences_original = results_original[2]
    
    # Calculate the readability of the simplified text
    results_simplified = calculate_readability(response)
    readability_simplified = results_simplified[0]
    num_words_simplified = results_simplified[1]
    num_sentences_simplified = results_simplified[2]
    
    # Save the statistics in a excel file
    
    data = {
        "Original Text": [text],
        "Simplified Text": [response],
        "Readability Original": [readability_original],
        "Readability Simplified": [readability_simplified],
        "Words Original": [num_words_original],
        "Words Simplified": [num_words_simplified],
        "Sentences Original": [num_sentences_original],
        "Sentences Simplified": [num_sentences_simplified]
    }

    df = pd.DataFrame(data)
    file_path = "statistics.xlsx"

    if os.path.exists(file_path):
        # If the file exists, append the new data
        with pd.ExcelWriter(file_path, engine='openpyxl', mode='a', if_sheet_exists='overlay') as writer:
            df.to_excel(writer, index=False, header=False, startrow=writer.sheets['Sheet1'].max_row)
    else:
        # If the file does not exist, create a new file
        df.to_excel(file_path, index=False)


def graph_readability():
    # Read the statistics from the excel file
    df = pd.read_excel("statistics.xlsx")
    
    # Plot the readability scores
    plt.hist(df["Readability Original"], alpha=0.5, label="Original Text")
    plt.hist(df["Readability Simplified"], alpha=0.5, label="Simplified Text")
    plt.xlabel("Flesch-Kincaid Grade Level")
    plt.ylabel("Frequency")
    plt.legend(loc='upper right')
    plt.title("Readability of Original and Simplified Text")
    plt.show()

def clean(text, client):
    clean_text = prompted_request("You are a text cleaner, you will get a text with LaTeX artifacts. I want you to remove the artifacts and return the text without artifacts and without changing anything else.", text, client, max_tks=20000)
    return clean_text
    
def prompted_request(system_prompt, text, client, temp=0.7, max_tks=1000, model="gpt-3.5-turbo"):
    # Call the OpenAI API
    response = client.chat.completions.create(
        model=model,
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": text}
        ],
        temperature=temp,  # Adjust creativity level
        max_tokens=max_tks  # Adjust output length
    )
    print("Response received")
    print(response)
    # Extract the generated text
    return response.choices[0].message.content
