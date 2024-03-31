from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
from openai import OpenAI
from convo import getSymptomList, generate_clarifying_questions, generate_summary

client = OpenAI()

app = Flask(__name__)
CORS(app, origins=["http://localhost:3000"])

# to test OpenAPI connection
@app.route('/poem', methods=['GET', 'POST'])
def getPoem():

    completion = client.chat.completions.create(
        model="gpt-3.5-turbo",
        max_tokens=100,
        messages=[
            {"role": "system", "content": "You are a poetic assistant, skilled in explaining complex programming concepts with creative flair."},
            {"role": "user", "content": "Compose a poem that explains the concept of recursion in programming."}
        ]
    )

    return str(completion.choices[0].message.content)

@app.route('/input', methods=['GET', 'POST'])
def getInput():
    return render_template('index.html')
    

# change to allow for input/output with react
# run convo.py to test backend
@app.route('/convo', methods=['GET', 'POST'])
def getConvo():
    print("How do you feel today? You can say things like 'my stomach hurts' or 'I feel sad'.")
    user_input = input().strip().lower()

    conversation_symptoms = []
    asked_symptoms = set()
    asked_questions = {}
    user_concerns = []

    while user_input.lower() not in ['exit', 'quit', 'no', 'nothing', 'none', 'stop', 'bye', 'goodbye', "that's all", "that's it"]:
        top_symptoms = getSymptomList(user_input, top_n=5, threshold=0.05)

        symptoms_to_ask = [symptom for symptom in top_symptoms if symptom not in asked_symptoms]

        if symptoms_to_ask:
            for symptom in symptoms_to_ask:
                question = generate_clarifying_questions([symptom], user_input, asked_questions)
                if question:
                    print(question)
                    user_response = input().strip().lower()
                    if user_response.lower() in ['yes', 'yep', 'yeah', 'right', 'correct', 'true', 'details']:
                        conversation_symptoms.append(symptom)
                        user_concerns.append(user_input)
                        asked_symptoms.add(symptom)  # Move this line here
        else:
            print("I'm having a bit of trouble understanding. Can you describe it differently?")
            user_concerns.append(user_input)

        print("Is there anything else you want to tell me?")
        user_input = input().strip().lower()

    unique_symptoms = set(conversation_symptoms)
    all_relevant_symptoms = set()

    for input_text in user_concerns:
        symptoms = getSymptomList(input_text, top_n=5, threshold=0.05)
        all_relevant_symptoms.update(symptoms)

    all_symptoms = unique_symptoms.union(all_relevant_symptoms)

    print("Based on our conversation, these symptoms might be relevant to you:")
    print(", ".join(all_symptoms))
    print("\nHere are all the concerns you mentioned:")
    for concern in user_concerns:
        print("-", concern)
    
    print("\nSummary of your concerns:")
    summary = generate_summary(user_concerns)
    print(summary)

if __name__ == '__main__':
    app.run(debug=True)