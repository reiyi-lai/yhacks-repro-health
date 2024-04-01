from flask import Flask, request, jsonify
from flask_cors import CORS
from convo import generate_clarifying_questions, list_relevant_symptoms
from simCheck import getSymptomList

app = Flask(__name__)
CORS(app)  

@app.route('/initial_greeting', methods=['GET'])
def initial_greeting():
    greeting = "How do you feel today? You can say things like 'my stomach hurts' or 'I feel sad'."
    return jsonify({"greeting": greeting})

@app.route('/generate_clarifying_questions', methods=['POST'])
def handle_generate_clarifying_questions():
    data = request.json
    user_input = data.get('user_input', '')
    asked_questions = data.get('asked_questions', {})

    top_symptoms = getSymptomList(user_input, top_n=5, threshold=0.05)
    symptoms_to_ask = [symptom for symptom in top_symptoms if symptom not in asked_questions]

    question = None
    if symptoms_to_ask:
        question = generate_clarifying_questions(symptoms_to_ask, user_input, asked_questions)
    
    if not question:
        return jsonify({"error": "Unable to generate further questions"}), 404

    return jsonify({"question": question})

@app.route('/list_relevant_symptoms', methods=['POST'])
def handle_list_relevant_symptoms():
    data = request.json
    user_input = data.get('user_input', '')

    symptoms = list_relevant_symptoms(user_input)

    if not symptoms:
        return jsonify({"error": "No relevant symptoms found"}), 404

    return jsonify({"symptoms": symptoms})

if __name__ == "__main__":
    app.run(debug=True, port=5001)
