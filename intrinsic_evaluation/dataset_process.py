import codecs
import json
import os
import sys
from dotenv import load_dotenv
from openai import OpenAI
import pandas as pd

# Add base directory to path for imports
load_dotenv(dotenv_path='api.env')
dir_path = os.getenv('DIR_PATH')
sys.path.append(dir_path)
from optimizer import *

api_key = os.getenv('API_KEY') 
client = OpenAI(api_key=api_key)

def process(data, system_prompt, file):
    for text in data:
        try:
            response = prompted_request(system_prompt, text, client)
            save_statistics(text, response, file)
        except Exception as e:
            print(e)
            continue
    return


def main():
    # open excel file
    df = pd.read_excel(dir_path + "intrinsic_evaluation\\excel_stats\\input.xlsx")
    sysprompt_plaintext = "You are a text enhancement AI. Your main goal is to make the text simpler while keeping the main idea. You will also correct any grammatical errors and improve the text. You will not change the main idea of the text. You will not add any new information to the text."
    sysprompt_first_metric_based = "You are an expert in simplifying text while preserving its original meaning and information. Given the text below, rewrite it to significantly reduce its complexity based on the Flesch-Kincaid Grade Level metric. Avoid adding new information, and ensure that the text remains clear and true to its original intent. Use shorter sentences, simpler vocabulary, and clear structure to achieve this"
    sysprompt_second_metric_based = "You are an expert in enhancing the readability of texts while preserving its original meaning and information. Given the text you receive, rewrite it to significantly reduce its complexity based on the Flesch-Kincaid Grade Level of the text."
    sysprompt_third_metric_based = "Your task is to reduce the Flesch-Kincaid Grade Level of texts. The Flesch-Kincaid Grade Level is calculated using the formula: Grade Level = 0.39 * (Total Words / Total Sentences) + 11.8 * (Total Syllables / Total Words) - 15.59. Given a text, rewrite it to significantly reduce its complexity by focusing on: Simplifying sentence structures; Using fewer syllables per word; Reducing the average sentence length. Ensure the rewritten text maintains its original meaning while achieving a much lower grade level."
    data = df["Original Text"].to_list()
    process(data, sysprompt_plaintext, "statistics_plaintext.xlsx")
    process(data, sysprompt_first_metric_based, "statistics_first_metric_based.xlsx")
    process(data, sysprompt_second_metric_based, "statistics_second_metric_based.xlsx")
    process(data, sysprompt_third_metric_based, "statistics_third_metric_based.xlsx")
    return


if __name__ == '__main__':
    main()
