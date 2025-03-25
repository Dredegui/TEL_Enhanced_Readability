import codecs
import json
import os
import random
import clean_latex
import sys
from dotenv import load_dotenv

load_dotenv(dotenv_path='api.env')
dir_path = os.getenv('DIR_PATH')
sys.path.append(dir_path)
from optimizer import *


def save_results(papers, results):
    data = {
        "papers": papers,
        "Original Text": results
    }
    df = pd.DataFrame(data)
    file_path = dir_path + "cleaned_input_test.xlsx"
    df.to_excel(file_path, index=False)
    return

def process_chunks(data, sample_size=2000, mode="random"):
    keys = list(data.keys())
    print("Number of papers: ", len(keys))
    if mode == "random":
        keys = random.sample(keys, len(keys))
    papers = []
    results = []
    i = -1
    while len(results) < sample_size and i < len(keys):
        i +=1
        try:
            paper = keys[i]
            print(paper)
            temp = data[paper]
            tex_list = temp["tex_data"]
            tex_list = clean_latex.extract_old(tex_list)
            # print(''.join(tex_list))
            clean_text = clean_latex.extract(tex_list)
            original_text = ''.join(tex_list)
            print("Original Text Length: ", len(original_text))
            print("Cleaned Text Length: ", len(clean_text))
            if len(clean_text) < 0.5 * len(original_text):
                continue
            papers.append(paper)
            results.append(clean_text)
            # print(clean_text)
        except Exception as e:
            save_results(papers, results)
            print(e)
            continue
    if i >= len(keys):
        print("Reached end")
    save_results(papers, results)
    return


def main():
    file_path = dir_path + "AAPR_Dataset\\data1"
    with codecs.open(file_path, 'r', 'utf-8') as f:
        data = json.load(f)
        process_chunks(data)
    return None

if __name__ == '__main__':
    main()
