# -*- coding: utf-8 -*-
"""
Created on Fri Dec 29 18:23:37 2017

@author: ypc
"""

import re
import os
import codecs
import tarfile
import json as js
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
nltk.download('stopwords')
nltk.download('punkt_tab')
english_stopwords = stopwords.words('english')


def clean_math(string):
    while string.count('$') > 1:
        pos0 = string.find('$')
        pos1 = string.find('$', pos0+1)
        string = (string[:pos0] + string[pos1+1:]).strip()
    return string

def remove_latex_commands(latex_text):
    # Remove Latex commands (e.g., \command{arg}{arg})
    latex_text = re.sub(r'\\[a-zA-Z]+\{[^\}]*\}\{[^\}]*\}', '', latex_text)

    # Remove LaTeX commands (e.g., \command{arg} or \command[arg])
    latex_text = re.sub(r'\\[a-zA-Z]+(?:\[[^\]]*\])?(?:\{[^\}]*\})?', '', latex_text)
    
    # Remove LaTeX environments (e.g., \begin{env} ... \end{env})
    latex_text = re.sub(r'\\begin\{[^}]+\}.*?\\end\{[^}]+\}', '', latex_text, flags=re.DOTALL)

    # Remove inline math ($...$) and display math (\[...\] or $$...$$)
    latex_text = re.sub(r'\$\$.*?\$\$', '', latex_text, flags=re.DOTALL)  # Display math
    latex_text = re.sub(r'\\\[.*?\\\]', '', latex_text, flags=re.DOTALL)  # Display math
    latex_text = re.sub(r'\$.*?\$', '', latex_text)  # Inline math
    
    # Remove comments
    latex_text = re.sub(r'%.*', '', latex_text)
    
    # Remove extra spaces and newlines
    # latex_text = re.sub(r'\s+', ' ', latex_text).strip()

    # if line.startswith('%') or line.startswith('\\') or line == '':
    # # Match \begin{...} and \end{...} to ignore content
    # if re.match(r'\\begin\{.*\}', line) and not ignore:
    #     ignore = True
    #     # Save the term to ignore which is \begin{ignore_term}
    #     ignore_term = re.match(r'\\begin\{(.*)\}', line).group(1)
    #     print(ignore_term)
    # elif re.match(r'\\end\{.*\}', line):
    #     print(line)
    #     ignore = False

    return latex_text        

def clean_str(string):
    """
    Input:
        string: One line in a latex file.
    Return：
        string cleaned.
    """
    
    string = clean_math(string)

    # Remove "ref" 
    string = re.sub(r'~(.*)}', '', string)
    string = re.sub(r'\\cite(.*)}', '', string)
    string = re.sub(r'\\newcite(.*)}', '', string)
    string = re.sub(r'\\ref(.*)}', '', string)

    # Replace intire string with empty string if it contains } at the end
    if string.endswith('}'):
        string = ''
    
    return string
    
    
def process_text_list(text_list):
    """
    Input:
        text_list: Content of a latex file and each element represents a line.
    Return:
        A string, which is the cleaned content of the latex file.
    """
    result = ''
    ignore = False
    ignore_math = False
    ignore_term = ''
    started = False
    for line in text_list:
        line = line.strip()
        # Ignore lines until document starts aka when it has \section{Introduction}
        intro_match = re.search(r'\\section', line) and re.search(r'Introduction', line)
        if intro_match and not started:
            started = True
        elif not started:
            continue
        # print("State\n ignore: " + str(ignore) + " ignore_math: " + str(ignore_math) + " ignore_term: " + ignore_term)
        # print("Line: " + line)
        if line.startswith('%') or line == '':
            continue
        if line.startswith('\\'):
            # Match \begin{...} and \end{...} to ignore content
            try:
                if re.match(r'\\begin\{.*\}', line) and not ignore:
                    ignore = True
                    # Save the term to ignore which is \begin{ignore_term}
                    ignore_term = re.match(r'\\begin\{(.*?)\}', line).group(1)
                # Match \end{ignore_term} to stop ignoring content
                if re.search(r'\\end\{' + ignore_term + '\}', line):
                    ignore = False
                # Match \[ and \] to ignore math content
                if re.match(r'\\\[', line):
                    ignore_math = True
                if re.search(r'\\\]', line):
                    ignore_math = False
                continue
            except Exception as e:
                # Make a custom exception
                e = Exception(str(e) + ' - ignore_term: ' + ignore_term)
                # Throw the exception
                raise e
        else:
            if ignore or ignore_math:
                continue
            result += clean_str(line) + ' '

    return result

def extract(tex_list, segment=False):
    data = tex_list
    return process_text_list(data)

# Extract Introduction, related work, etc.================================================================
def split(tex_list, start_char, end_char):
    lines = tex_list
    length = len(lines)
    start = None
    end = None
    i = 0
    while i < length and (end is None):
        if start is None:
            if lines[i].startswith(start_char):
                start = i
        else:
            if lines[i].startswith(end_char):
                end = i
        i += 1
    if (start is not None) and (end is None):
        end = length
    return lines[start:end]

def extract_old(tex_list, segment=False):
    data = tex_list
    intro = ' '.join(split(tex_list, '\section{Intro', '\section{'))
    # related = ' '.join(split(tex_list, '\section{Related', '\section{'))
    # conclusion = ' '.join(split(tex_list, '\section{Conclu', '\section{'))
    # methods = text.replace(intro, '').replace(related, '').replace(conclusion, '')
    if segment:
        pass
    else:
        return intro.split('\n')
    