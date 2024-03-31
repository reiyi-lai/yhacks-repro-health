 #checks similarity of user input with symptoms list
#import nltk
from nltk.stem import PorterStemmer
import iknowpy
from sentence_transformers import SentenceTransformer, util

#nltk.download()


import csv

symptoms_list = []

# Load and preprocess symptoms from CSV
with open('symptoms.csv', mode='r') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        symptoms = row['Symptoms'].split(', ')
        for symptom in symptoms:
            if symptom not in symptoms_list:  # Check for duplicates
                symptoms_list.append(symptom)

# compute the embeddings of the symptoms_list
model = SentenceTransformer('all-MiniLM-L6-v2')
symptomEmbedding = model.encode(symptoms_list, convert_to_tensor=True)

# initialize the enginedef getSymptomList(userInput):
    # Initialize the stemmer and the iKnow engine
def getSymptomList(userInput):
    # Initialize the iKnow engine
    iknow = iknowpy.iKnowEngine()

    # Index the user input to extract meaningful entities
    iknow.index(userInput, "en")
    extracted_terms = []

    # Extract concepts or relations as they likely represent symptoms
    for sentence in iknow.m_index['sentences']:
        for entity in sentence['entities']:
            if entity['type'] in ['Concept', 'Relation']:
                extracted_terms.append(entity['text'])  # Use the full text instead of stemmed version

    # Encode the extracted terms to vectors
    patient_embeddings = model.encode(extracted_terms, convert_to_tensor=True)

<<<<<<< HEAD
    relevant_symptoms = set()
    threshold = 0.4  # Adjust the threshold based on testing
=======
    userSentence = ' '.join(words)
    #print(userSentence)
>>>>>>> c15e45de14136322f32063537ee49549df07d23d

    for patient_embedding in patient_embeddings:
        # Compute cosine similarities between user sentence embedding and symptom embeddings
        cosine_scores = util.cos_sim(patient_embedding, symptomEmbedding)

        for i in range(len(symptoms_list)):
            if cosine_scores[0][i] > threshold:
                relevant_symptoms.add(symptoms_list[i])

<<<<<<< HEAD
    return list(relevant_symptoms) if relevant_symptoms else ["No clear symptom identified"]
=======
    #Compute cosine-similarities
    cosine_scores = util.cos_sim(patientEmbedding, symptomEmbedding)

    #Output the pairs with their score
    scores = dict()
    for i in range(len(symptoms_list)):
        scores[symptoms_list[i]] = cosine_scores[0][i]
    
    scores = sorted(scores.items(), reverse=True, key=lambda x:x[1])
    #print("Similar symptom calculated: " + str(scores[0][0]))

    #only return most relevant symptom as string
    return scores[0][0]


# test different user inputs:
# getSymptomList("I have pain when I pee")
# print("\n")

# getSymptomList("My stomach hurts")
>>>>>>> c15e45de14136322f32063537ee49549df07d23d
