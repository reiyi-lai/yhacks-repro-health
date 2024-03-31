#conversation 

from openai import OpenAI
import json
import nltk
import simCheck

#nltk.download('all')
client = OpenAI()

clarifying_questions = {
    "general": [
        "How long have you been experiencing this symptom?",
        "Is the pain constant or does it come and go?"
    ],
    "pain_intensity": [
        "On a scale from 1 to 10, how would you rate your pain?",
        "Does anything make the pain better or worse?"
    ],
    "location_specific": {
        "headache": [
            "Is the pain localized to one side of your head or all over?",
            "Do you experience sensitivity to light or noise?"
        ],
        "abdominal": [
            "Is the pain more towards the upper or lower part of your abdomen?",
            "Does the pain spread to any other part of your body?"
        ]
    }
}

def generate_clarifying_questions(user_input):
    prompt = f"""Given the user's input about their symptoms, respond with a question to clarify the user's symptom. User input: "{user_input}" """

    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        max_tokens=500,
        messages=[
            {"role": "system", "content": "You are a healthcare assistant trying to help patients clarify their symptoms"},
            {"role": "user", "content": prompt}
        ]
    )
    return nltk.sent_tokenize(response.choices[0].message.content)

def generate_longevity_question(user_input):
    prompt = f"""Given the user's input about their symptoms, respond with a question to clarify how long the user's symptom has been ongoing. User input: "{user_input}" """

    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        max_tokens=500,
        messages=[
            {"role": "system", "content": "You are a healthcare assistant trying to determine how long the patients has been experiencing their symptom"},
            {"role": "user", "content": prompt}
        ]
    )
    return nltk.sent_tokenize(response.choices[0].message.content)

def main():

    user_responses = {}

    print("How are you feeling today?")
    user_input = input()

    while True:
        if user_input.lower() in ['exit', 'quit', 'no' 'nothing', 'none', 'stop', 'good', 'great', 'bye', 'goodbye','fine', 'okay', 'well', 'nothing wrong', 'all good', 'no problems', 'no issues', 'excellent', 'splendid']:
            print("Take care! If you have any more concerns, feel free to talk to me.")
            break

        questions = generate_clarifying_questions(user_input)
        for question in questions:
            print(question)
            user_input = input().strip().lower()
            user_responses[question] = user_input
        
        questions2 = generate_longevity_question(user_input)
        for question2 in questions2:
            print(question2)
            user_input = input().strip().lower()
            user_responses[question2] = user_input  

        print("What else would you like to note?")
        user_input = input().strip().lower()
    
            

main()