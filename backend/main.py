from flask import Flask, request, jsonify
import openai

app = Flask(__name__)

# Set your OpenAI API key


@app.route('/chatbot', methods=['POST'])
def chatbot():
    # Get user input from the request
    user_input = request.json['message']

    # Use the OpenAI API to generate a response
    response = openai.Completion.create(
        engine="text-davinci-002",  # Choose the language model engine
        prompt=user_input,
        max_tokens=50  # Adjust as needed
    )

    bot_response = response.choices[0].text.strip()

    # Return the response to the user
    return jsonify({'message': bot_response})

if __name__ == '__main__':
    app.run(debug=True)