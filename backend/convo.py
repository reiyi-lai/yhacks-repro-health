from openai import OpenAI
#import nltk
from nltk.tokenize import word_tokenize
from transformers import AutoTokenizer, AutoModel
import torch
import csv

<<<<<<< HEAD

model_name = "sentence-transformers/all-MiniLM-L6-v2"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModel.from_pretrained(model_name)
=======
from openai import OpenAI
import json
import nltk
import simCheck

#nltk.download('all')
client = OpenAI()
>>>>>>> 155e5d4964a49eb7192154958a9d482b457f2dd5

symptomsList = []
diseasesList = []
dsMap = {}  # Disease symptoms map

<<<<<<< HEAD
# Load and preprocess symptoms and diseases from CSV
with open('symptoms.csv', mode='r') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        diseasesList.append(row['Disease Name'])
        symptoms = row['Symptoms'].split(', ')
        dsMap[row['Disease Name']] = symptoms
        for symptom in symptoms:
            if symptom not in symptomsList:  # Check for duplicates
                symptomsList.append(symptom)

# Function to process symptoms for better matching
def processed_symptoms(symptomsList):
    processed = {}
    for symptom in symptomsList:
        words = set(word_tokenize(symptom.lower()))
        processed[symptom] = words
    return processed

processed_symptoms = processed_symptoms(symptomsList)

# Function to match user description to closest symptom
def match_symptom(user_desc, processed_symptoms):
    user_input_tokens = tokenizer(user_desc, return_tensors="pt", padding=True, truncation=True, max_length=512)
    user_input_embeddings = model(**user_input_tokens).pooler_output

    best_symptom = None
    highest_similarity = -1

    for symptom, _ in processed_symptoms.items():
        symptom_tokens = tokenizer(symptom, return_tensors="pt", padding=True, truncation=True, max_length=512)
        symptom_embeddings = model(**symptom_tokens).pooler_output
        similarity = torch.cosine_similarity(user_input_embeddings, symptom_embeddings).item()

        if similarity > highest_similarity:
            best_symptom = symptom
            highest_similarity = similarity

    return best_symptom

# Function to generate clarifying questions based on matched symptom
def generate_clarifying_questions_openai(user_input):
    prompt = f"What clarifying questions can be asked to understand more about '{user_input}'?"
    response = OpenAI.Completion.create(
        model="text-davinci-003",
        prompt="Your prompt here",
        temperature=0.5,
        max_tokens=100,
        frequency_penalty=0.0,
        presence_penalty=0.0
    )
    clarifying_questions = [choice.text.strip() for choice in response.choices]
    return clarifying_questions

# Function to generate clarifying questions based on matched symptom
def generate_clarifying_questions(user_input):
    matched_symptom = match_symptom(user_input, processed_symptoms)
    potential_diseases = [disease for disease, symptoms in dsMap.items() if matched_symptom in symptoms]
=======
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
>>>>>>> 155e5d4964a49eb7192154958a9d482b457f2dd5

    clarifying_questions = []
    for disease in potential_diseases:
        for symptom in dsMap[disease]:
            if symptom != matched_symptom:  # Avoid asking about the matched symptom again
                clarifying_questions.append(f"Do you also experience {symptom.lower()}? (Yes/No)")

    clarifying_questions.append("Is there anything else you're experiencing or feel is important to mention?")
    return clarifying_questions

# Function to compile user's symptoms into a summary
def compile_user_symptoms(user_responses):
    confirmed_symptoms = [symptom for symptom, response in user_responses.items() if response == 'yes']
    if confirmed_symptoms:
        return "Your symptoms in medical terms are: " + ", ".join(confirmed_symptoms)
    else:
        return "No specific symptoms were confirmed."

# Main interaction function
def main():
<<<<<<< HEAD
    print("Why do you not feel well today?")
    user_input = input().lower()

    if user_input in ['exit', 'quit', 'stop']:
        print("Take care! If you have any more concerns, feel free to talk to me.")
        return
    
    clarifying_questions = generate_clarifying_questions_openai(user_input)
    user_responses = {}

    for question in clarifying_questions:
        print(question)
        answer = input("Your answer (Yes/No): ").strip().lower()
        user_responses[question] = answer

    symptoms_summary = compile_user_symptoms(user_responses)
    print(symptoms_summary)

if __name__ == "__main__":
    main()
=======

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
>>>>>>> 155e5d4964a49eb7192154958a9d482b457f2dd5
