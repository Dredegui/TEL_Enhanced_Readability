from dotenv import load_dotenv
import os
from openai import OpenAI
from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
from optimizer import *


load_dotenv(dotenv_path='api.env')
api_key = os.getenv('API_KEY') 
client = OpenAI(api_key=api_key)
app = Flask(__name__)
CORS(app)

# system_prompt = "You are a text enhancement AI. Your main goal is to make the text simpler while keeping the main idea. You will also correct any grammatical errors and improve the text. You will not change the main idea of the text. You will not add any new information to the text."
# system_prompt = "You reduce the Flesch-Kincaid Grade Level of texts. Given the text you receive, rewrite it to significantly reduce its complexity based on the Flesch-Kincaid Grade Level of the text."
# system_prompt = "You reduce the Flesch-Kincaid Grade Level of texts. Given the text you receive, rewrite it to significantly reduce its complexity based on the Flesch-Kincaid Grade Level of the text."
# ^ These prompts have good performance. 

# system_prompt = "You are an expert in simplifying text while preserving its original meaning and information. Given the text below, rewrite it to significantly reduce its complexity based on the Flesch-Kincaid Grade Level metric. Avoid adding new information, and ensure that the text remains clear and true to its original intent. Use shorter sentences, simpler vocabulary, and clear structure to achieve this."
# ^ This prompt has ok performance. But it simplifies the text too much.

# system_prompt = "You are an expert in enhancing the readability of texts while preserving its original meaning and information. Given the text you receive, rewrite it to significantly reduce its complexity based on the Flesch-Kincaid Grade Level of the text."
# ^ This prompt has horrible performance. 

system_prompt = "Your task is to reduce the Flesch-Kincaid Grade Level of texts. The Flesch-Kincaid Grade Level is calculated using the formula:  Grade Level = 0.39 * (Total Words / Total Sentences) + 11.8 * (Total Syllables / Total Words) - 15.59. Given a text, rewrite it to significantly reduce its complexity by focusing on:  Simplifying sentence structures; Using fewer syllables per word; Reducing the average sentence length. Ensure the rewritten text maintains its original meaning while achieving a much lower grade level."

@app.route('/enhance', methods=['POST'])
def enhance_text():
    print("Request received")
    data = request.json
    prompt = "Enhance the following text:"
    text = data['text']
    response = prompted_request(prompt, system_prompt, text, client)
    print("Saving statistics")  
    save_statistics(text, response)
    return jsonify({'response': response})

@app.route('/')
def index():
    return render_template('index.html') 

if __name__ == '__main__':
    app.run(debug=True)