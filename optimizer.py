from dotenv import load_dotenv
import os
from openai import OpenAI
from flask import Flask, request, jsonify, render_template
from flask_cors import CORS


load_dotenv(dotenv_path='api.env')
api_key = os.getenv('API_KEY') 
client = OpenAI(api_key=api_key)
app = Flask(__name__)
CORS(app)

system_prompt = "You are a text enhancement AI. You are given a text prompt and you enhance it. The main goal is to make the text simpler while keeping the main idea. You will also correct any grammatical errors and improve the text. You will not change the main idea of the text. You will not add any new information to the text."

def prompted_request(prompt, text, model="gpt-4o"):
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
        max_tokens=500  # Adjust output length
    )
    
    # Extract the generated text
    return response['choices'][0]['message']['content']


@app.route('/enhance', methods=['POST'])
def enhance_text():
    print("Request received")
    data = request.json
    prompt = "Enhance the following text:"
    text = data['text']
    response = prompted_request(prompt, text)
    return jsonify({'response': response})

@app.route('/')
def index():
    return render_template('index.html') 

if __name__ == '__main__':
    app.run(debug=True)