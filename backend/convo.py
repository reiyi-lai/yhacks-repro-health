#conversation 

import openai
import json
import nltk

nltk.download('all')

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
    prompt = f"""Given the user's input about their symptoms, generate a series of clarifying questions to better understand their condition. User input: "{user_input}" """

    response = openai.Completion.create(
        engine="davinci",
        prompt=prompt,
        temperature=0.7,
        max_tokens=150,
        top_p=1,
    )

    return nltk.sent_tokenize(response.choices[0].text)

def main():
    print("How are you feeling today?")
    while True:
        user_input = input()
        if user_input.lower() in ['exit', 'quit', 'stop', 'good', 'great', 'bye', 'goodbye','fine', 'okay', 'well', 'nothing wrong', 'all good', 'no problems', 'no issues', 'excellent', 'splendid']:
            print("Take care! If you have any more concerns, feel free to talk to me.")
            break

        clarifyQuestions = generate_clarifying_questions(user_input)
        for question in clarifyQuestions:
            print(f"{question}")
            input(" ")