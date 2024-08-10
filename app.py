from flask import Flask, render_template, request, jsonify
from flask_cors import CORS
import openai
import config

app = Flask(__name__)
CORS(app)

# Set up OpenAI API key
openai.api_key = config.OPENAI_API_KEY

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/get', methods=['POST'])
def chatbot_response():
    user_input = request.json['msg']
    try:
        # Use the updated OpenAI API for ChatCompletion
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",  # Use gpt-4 if available
            messages=[
                {"role": "system", "content": "You are a helpful assistant focused on relieving stress."},
                {"role": "user", "content": user_input}
            ]
        )
        # Extract the assistant's reply
        reply = response['choices'][0]['message']['content']
    except Exception as e:
        print("Error connecting to OpenAI:", e)
        reply = "Sorry, I'm having trouble connecting to OpenAI. Please try again later."
    return jsonify(reply)

if __name__ == "__main__":
    app.run(debug=True)
