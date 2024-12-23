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
    avg_words_per_sentence = len(words) / len(sentences)
    
    # Calculate the average number of syllables per word
    syllables = 0
    for word in words:
        syllables += syllapy.count(word)
    avg_syllables_per_word = syllables / len(words)
    
    # Calculate the Flesch-Kincaid Grade Level
    flesch_kincaid = 0.39 * avg_words_per_sentence + 11.8 * avg_syllables_per_word - 15.59
    return flesch_kincaid

def save_statistics(text, response):
    # Calculate the readability of the original text
    readability_original = calculate_readability(text)
    
    # Calculate the readability of the enhanced text
    readability_enhanced = calculate_readability(response)
    
    # Save the statistics in a excel file
    
    data = {
        "Original Text": [text],
        "Enhanced Text": [response],
        "Readability Original": [readability_original],
        "Readability Enhanced": [readability_enhanced]
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
    plt.hist(df["Readability Enhanced"], alpha=0.5, label="Enhanced Text")
    plt.xlabel("Flesch-Kincaid Grade Level")
    plt.ylabel("Frequency")
    plt.legend(loc='upper right')
    plt.title("Readability of Original and Enhanced Text")
    plt.show()

    

def prompted_request(prompt, system_prompt, text, client, model="gpt-3.5-turbo"):
    # Combine prompt and input text
    full_prompt = f"{prompt}\n\n{text}"
    # Call the OpenAI API
    response = client.chat.completions.create(
        model=model,
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": full_prompt}
        ],
        temperature=0.7,  # Adjust creativity level
        max_tokens=1000  # Adjust output length
    )
    print("Response received")
    print(response)
    # Extract the generated text
    return response.choices[0].message.content
