import codecs
import json
import os
from optimizer import *
from dotenv import load_dotenv
from openai import OpenAI
import clean_latex

system_prompt = "You are an expert in simplifying text while preserving its original meaning and information. Given the text below, rewrite it to significantly reduce its complexity based on the Flesch-Kincaid Grade Level metric. Avoid adding new information, and ensure that the text remains clear and true to its original intent. Use shorter sentences, simpler vocabulary, and clear structure to achieve this."
prompt = "Enhance the following text:"

load_dotenv(dotenv_path='api.env')
api_key = os.getenv('API_KEY') 
client = OpenAI(api_key=api_key)

def process_chunks(data, start=0, sample_size=100):
    keys = list(data.keys())
    # remove data* keys from list
    keys = [i for i in keys if not i.startswith('data')]
    papers = []
    results = []
    results_cleaned = []
    i = -1
    while len(results) < sample_size:
        i +=1
        try:
            paper = keys[i]
            print(paper)
            temp = data[paper]
            tex_list = temp["tex_data"]
            # print(''.join(tex_list))
            clean_text = clean_latex.extract(tex_list)
            original_text = ''.join(tex_list)
            print("Original Text Length: ", len(original_text))
            print("Cleaned Text Length: ", len(clean_text))
            if len(clean_text) < 0.4 * len(original_text):
                continue
            extra_cleaned_text = clean(clean_text, client)
            papers.append(paper)
            results.append(clean_text)
            results_cleaned.append(extra_cleaned_text)
            print("Extra Cleaned Text Length: ", len(extra_cleaned_text))
            # print(clean_text)
        except Exception as e:
            print(e)
            continue
    data = {
        "papers": papers,
        "Original Text": results,
        "Cleaned Text": results_cleaned
    }
    df = pd.DataFrame(data)
    file_path = "C:\\Users\\guipa\\OneDrive\\Documentos\\GitHub\\TEL_Enhanced_Readability\\cleaned_input.xlsx"
    df.to_excel(file_path, index=False)
    return



def main():
    file_path = "C:\\Users\\guipa\\OneDrive\\Documentos\\GitHub\\TEL_Enhanced_Readability\\AAPR_Dataset\\data1"
    with codecs.open(file_path, 'r', 'utf-8') as f:
        data = json.load(f)
        process_chunks(data)
    return None

if __name__ == '__main__':
    main()
