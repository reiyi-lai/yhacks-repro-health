<<<<<<< HEAD
from openai import OpenAI
import json
import nltk
from simCheck import getSymptomList  # Assuming simCheck is a custom module you have access to

# Ensure necessary NLTK data is downloaded
#nltk.download('punkt')

client = OpenAI()

def generate_clarifying_questions(user_input):
    prompt = f"""Given the user's input about their symptoms, respond with a question that is easy to understand to clarify the user's symptom. User input: "{user_input}" """
    
    try:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            max_tokens=500,
            messages=[
                {"role": "system", "content": "You are a healthcare assistant trying to help non-native English speaking patients clarify their symptoms. Don't ask about how long they have had the symptoms"},
                {"role": "user", "content": prompt}
            ]
        )
        return nltk.sent_tokenize(response.choices[0].message.content)
    except Exception as e:
        print(f"An error occurred: {e}")
        return []

def main():
    user_responses = {}

    print("How are you feeling today?")
    user_input = input().strip().lower()

    while True:
        if user_input in ['exit', 'quit', 'no', 'nothing', 'none', 'stop', 'good', 'great', 'bye', 'goodbye', 'fine', 'okay', 'well', 'nothing wrong', 'all good', 'no problems', 'no issues', 'excellent', 'splendid', "that's all", "that's it"]:
            break
        
        questions = generate_clarifying_questions(user_input)
        for question in questions:
            print(question)
            user_response = input().strip().lower()
            user_responses[question] = user_response
        
        print("What else would you like to add?")
        user_input = input().strip().lower()
    
    if user_responses:
        final_symptoms = []
        for response in user_responses.values():
            symptoms_from_response = getSymptomList(response)
            
            # Check if the return value is a string instead of a list
            if isinstance(symptoms_from_response, str):
                # If it's a string, add it directly to the list
                final_symptoms.append(symptoms_from_response)
            else:
                # If it's a list, extend the list with these symptoms
                final_symptoms.extend(symptoms_from_response)
        
        # Join the symptoms with ", " to print them out as a comma-separated list
        symptoms_string = ", ".join(final_symptoms)
        
        print("Here are the symptoms we've determined that you have mentioned:")
        print(symptoms_string)
    else:
        print("No symptoms identified. If you're feeling unwell, please consult a healthcare professional.")


if __name__ == "__main__":
    main()
=======
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
            {"role": "system", "content": "You are a healthcare assistant trying to help patients clarify their symptoms. Don't ask about how long they have had the symptoms"},
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
        
        # questions2 = generate_longevity_question(user_input)
        # for question2 in questions2:
        #     print(question2)
        #     user_input = input().strip().lower()
        #     user_responses[question2] = user_input  

        print("What else would you like to note?")
        user_input = input().strip().lower()
    
    finalSymptoms = []
    for response in user_responses.values():
        finalSymptoms.append(simCheck.getSymptomList(response))
    
    print("Here are the symptoms we've determined you have mentioned:")
    for symptom in finalSymptoms:
        print(symptom, end=", ")
    
            

main()
>>>>>>> c15e45de14136322f32063537ee49549df07d23d
