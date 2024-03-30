#conversation 

import openai
import json
import nltk

nltk.download('all')


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
        user_input = input("User: ").strip()
        if user_input.lower() in ['exit', 'quit', 'stop', 'good', 'great']:
            print("AI: Take care! If you have any more concerns, feel free to talk to me.")
            break

        clarifyQuestions = generate_clarifying_questions(user_input)
        for question in clarifyQuestions:
            print(f"{question}")
            input(" ")