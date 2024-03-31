from openai import OpenAI
import json
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

    unasked_question_types = [q_type for q_type in question_types if symptom not in asked_questions or q_type not in asked_questions[symptom]]

    if not unasked_question_types:
        return None  # If all types of questions have been asked, don't repeat

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

def main():
    print("How do you feel today? You can say things like 'my stomach hurts' or 'I feel sad'.")
    user_input = input().strip().lower()

    conversation_symptoms = []  # To store symptoms that have been discussed
    asked_symptoms = set()  # Track symptoms that have been inquired about
    asked_questions = set()  # Track specific questions that have been asked


    while user_input.lower() not in ['exit', 'quit', 'no', 'nothing', 'none', 'stop', 'bye', 'goodbye', "that's all", "that's it"]:
        top_symptoms = getSymptomList(user_input, top_n=5, threshold=0.2)  # Use updated getSymptomList function

        # Filter out symptoms that have already been asked about
        symptoms_to_ask = [symptom for symptom in top_symptoms if symptom not in asked_symptoms]

        if symptoms_to_ask:
            for symptom in symptoms_to_ask:
                # Generate and ask a clarifying question for each new symptom
                question = generate_clarifying_questions([symptom], user_input, asked_questions)
                if question:  # Ensure the question is new and was not previously asked
                    print(question)
                    user_response = input().strip().lower()
                    if user_response.lower() in ['yes', 'yep', 'yeah', 'right', 'correct', 'true', 'details']:
                        conversation_symptoms.append(symptom)
                    asked_symptoms.add(symptom)
        else:
            print("I'm having a bit of trouble understanding. Can you describe it differently?")

        print("Is there anything else you want to tell me?")
        user_input = input().strip().lower()

    if conversation_symptoms:
        unique_symptoms = set(conversation_symptoms)  # Remove duplicates
        print("Based on our conversation, these symptoms might be relevant to you:")
        print(", ".join(unique_symptoms))
    else:
        print("Okay, if you ever want to talk, I'm here.")

if __name__ == "__main__":
    main()
