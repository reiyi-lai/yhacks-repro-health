from transformers import AutoTokenizer, AutoModel
import torch
import csv
from openai import OpenAI
import nltk

# nltk.download('punkt')

client = OpenAI()

model_name = "sentence-transformers/all-MiniLM-L6-v2"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModel.from_pretrained(model_name)

symptomsList = []
diseasesList = []
dsMap = {}  # Disease symptoms map

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
        words = set(nltk.word_tokenize(symptom.lower()))
        processed[symptom] = words
    return processed

processed_symptoms = processed_symptoms(symptomsList)

# Function to match user description to closest symptom
def match_symptom(user_desc, processed_symptoms, tokenizer, model):
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
def generate_clarifying_questions_openai(user_input, client):
    prompt = f"""Given the user's input about their symptoms, What easy to understand clarifying questions can be asked to understand more about '{user_input}'? """
    response = client.chat.completions.create(
        model="text-davinci-003",
        max_tokens=500,
        messages=[
            {"role": "system", "content": "You are a healthcare assistant trying to help patients who are non-Native English speakers clarify their symptoms."},
            {"role": "user", "content": prompt}
        ]
    )

    # Extracting the 'text' from each 'Choice' object
    clarifying_questions = [choice['message']['content'].strip() for choice in response['choices']]
    return clarifying_questions


# Function to generate clarifying questions based on matched symptom
def generate_clarifying_questions(user_input):
    matched_symptom = match_symptom(user_input, processed_symptoms, tokenizer, model)
    potential_diseases = [disease for disease, symptoms in dsMap.items() if matched_symptom in symptoms]
    prompt = f"""Given the user's input about their symptoms, what clarifying questions can be asked to understand more about '{matched_symptom}'?"""

    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        max_tokens=500,
        messages=[
            {"role": "system", "content": "You are a healthcare assistant trying to help patients clarify their symptoms. Don't ask about how long they have had the symptoms"},
            {"role": "user", "content": prompt}
        ]
    )
    return nltk.sent_tokenize(response['choices'][0]['message']['content'])

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
    print("Why do you not feel well today?")
    user_input = input().lower()

    if user_input in ['exit', 'quit', 'stop']:
        print("Take care! If you have any more concerns, feel free to talk to me.")
        return
    
    clarifying_questions = generate_clarifying_questions_openai(user_input, client)
    user_responses = {}

    for question in clarifying_questions:
        print(question)
        answer = input("Your answer (Yes/No): ").strip().lower()
        user_responses[question] = answer

    symptoms_summary = compile_user_symptoms(user_responses)
    print(symptoms_summary)

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
