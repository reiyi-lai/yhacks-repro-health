from flask import Flask, request, jsonify
from openai import OpenAI

client = OpenAI()

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def main():

    completion = client.chat.completions.create(
        model="gpt-3.5-turbo",
        max_tokens=100,
        messages=[
            {"role": "system", "content": "You are a poetic assistant, skilled in explaining complex programming concepts with creative flair."},
            {"role": "user", "content": "Compose a poem that explains the concept of recursion in programming."}
        ]
    )

    return jsonify(str(completion.choices[0].message.content))

if __name__ == '__main__':
    app.run(debug=True)