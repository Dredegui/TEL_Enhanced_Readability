import codecs
import json
import os
from optimizer import *
from dotenv import load_dotenv
from openai import OpenAI

system_prompt = "You are an expert in simplifying text while preserving its original meaning and information. Given the text below, rewrite it to significantly reduce its complexity based on the Flesch-Kincaid Grade Level metric. Avoid adding new information, and ensure that the text remains clear and true to its original intent. Use shorter sentences, simpler vocabulary, and clear structure to achieve this."
prompt = "Enhance the following text:"

load_dotenv(dotenv_path='api.env')
api_key = os.getenv('API_KEY') 
client = OpenAI(api_key=api_key)

def process_chunks(data, start=0, chunk_size=100):
    keys = list(data.keys())
    # remove data* keys from list
    keys = [i for i in keys if not i.startswith('data')]
    for i in range(start, chunk_size):
        try:
            print(keys[i])
            temp = data[keys[i]]
            print(len(temp))
            # temp is a list of strings
            # use the first string 
            text = temp[0]
            clean_text = prompted_request("Incorrect text: ", "You are a text cleaner, you will get a text that has words stuck together, grammar errors, etc. You will return the same text but a correct version.", text, client)
            response = prompted_request(prompt, system_prompt, clean_text, client)
            save_statistics(clean_text, response)
        except Exception as e:
            print(e)
            continue
    return



def main():
    with codecs.open('dataset.json', 'r', 'utf-8') as f:
        data = json.load(f)
        process_chunks(data)
    return None

if __name__ == '__main__':
    main()
