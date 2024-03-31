from openai import OpenAI
import json
from random import shuffle
import random
import nltk
from simCheck import getSymptomList, symptoms_list  # Updated function name

# Ensure necessary NLTK data is downloaded
# nltk.download('punkt')

client = OpenAI()


def generate_clarifying_questions(symptoms, user_input, asked_questions):

    # Choose a random symptom from the list for simplicity or implement your logic
    symptom = symptoms[0] if symptoms else "your symptom"
    
    question_types = {
        "timing": "Does this happen all the time or more at certain times?",
        "trigger": "Does this seem to happen after certain activities or situations?",
        "intensity": "Is the feeling mild or strong?",
        "location": "Where exactly do you feel this?"
    }

    # Shuffle the question types to introduce randomness
    unasked_question_types = list(question_types.keys())
    random.shuffle(unasked_question_types)

    # Check if any question type for the symptom has been asked before
    if symptom in asked_questions:
        for q_type in unasked_question_types:
            if q_type not in asked_questions[symptom]:
                selected_question_type = q_type
                break
        else:
            # If all question types have been asked, return None
            return None
    else:
        # If no question has been asked for the symptom, select a random question type
        selected_question_type = random.choice(unasked_question_types)

    # Check if the question about this symptom was already asked
    if symptom in asked_questions:
        return None  # Skip asking about this symptom again

    
    prompt = f"""Given the user's simple description of how they feel, ask a simple question to know more and try to match how they feel with a symptom from {symptoms_list}. The clarifying question should help you narrow down the potential symptom it may be that the user is experiencing. The user said: "{user_input}" """

    try:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            max_tokens=500,
            messages=[
                {"role": "system", "content": "You are a helper trying to understand people's health problems using simple words because they do not know English well. Target audience is English as a second language immigrants and children."},
                {"role": "user", "content": prompt}
            ]
        )
        question = nltk.sent_tokenize(response.choices[0].message.content)[0]  # Return first sentence as question
        
        if symptom not in asked_questions:
            asked_questions[symptom] = []
        asked_questions[symptom].append(selected_question_type)

        return question

    except Exception as e:
        print(f"An error occurred: {e}")
        return "Can you describe that a bit more?"


def list_relevant_symptoms(user_input):
    prompt = f"The user mentioned '{user_input}'. Tell me the most relevant symptom from {symptoms_list}"
    for symptom in symptoms_list:
        if symptom.lower() in user_input.lower():
            prompt += f"- {symptom}\n"

    try:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo3",
            prompt=prompt,
            max_tokens=150,
            stop=["\n\n"],
            messages=[
                {"role": "system", "content": "You are a helper providing information about relevant symptoms to the user based on what they say"},
                {"role": "user", "content": user_input}
            ]
        )

        # Extracting the response from completion
        return response.choices[0].text.strip()
    except Exception as e:
        print(f"An error occurred: {e}")
        return "Unable to list relevant symptoms at the moment."

def main():
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


if __name__ == "__main__":
    main()
