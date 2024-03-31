from flask import Flask, request, jsonify
from flask_cors import CORS
from openai import OpenAI
import convo

client = OpenAI()

app = Flask(__name__)
CORS(app, origins=["http://localhost:3000"])

@app.route('/poem', methods=['GET', 'POST'])
def main():

    completion = client.chat.completions.create(
        model="gpt-3.5-turbo",
        max_tokens=100,
        messages=[
            {"role": "system", "content": "You are a poetic assistant, skilled in explaining complex programming concepts with creative flair."},
            {"role": "user", "content": "Compose a poem that explains the concept of recursion in programming."}
        ]
    )

    return str(completion.choices[0].message.content)

if __name__ == '__main__':
    app.run(debug=True)