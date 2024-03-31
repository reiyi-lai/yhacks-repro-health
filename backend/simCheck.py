import csv
from nltk.stem import PorterStemmer
import iknowpy
from sentence_transformers import SentenceTransformer, util


qualifiers = {
    "pain during sex": ["painful intercourse", "discomfort during sexual activity"],
    "vaginal bleeding": ["abnormal vaginal bleeding", "irregular menstrual bleeding", "irregular periods"],
    "blisters on the genitals": ["genital sores", "genital lesions", "fluid-filled bumps on the genitals"],
    "blisters on the rectum": ["rectal sores", "rectal lesions", "fluid-filled bumps around the anus"],
    "blisters on the mouth": ["oral sores", "canker sores", "cold sores", "fluid-filled bumps in the mouth"],
    "mouth ulcers": ["oral sores on the inside", "mouth bumps on the inside"],
    "frequent urination": ["urinating often", "increased urination frequency", "peeing alot"],
    "lower back pain": ["pain in the lumbar region", "discomfort in the lower back"],
    "infertility": ["difficulty conceiving", "reproductive challenges"],
    "heavy period": ["excessive menstrual bleeding", "prolonged menstrual flow"],
    "painful period": ["menstrual pain", "dysmenorrhea", "cramps"],
    "pain in lower abdomen": ["abdominal discomfort", "pelvic pain"],
    "painful bowel movements": ["discomfort during defecation", "pain during passing stool"],
    "acne": ["skin breakouts", "pimple formation"],
    "thin vaginal discharge": ["watery vaginal discharge", "clear vaginal secretions"],
    "white vaginal discharge": ["milky vaginal discharge", "thick white discharge"],
    "gray vaginal discharge": ["grayish vaginal discharge", "cloudy vaginal secretions"],
    "yellow vaginal discharge": ["yellowish vaginal discharge", "yellow-colored discharge"],
    "thick vaginal discharge": ["viscous vaginal discharge", "dense vaginal secretions"],
    "foul smelling vaginal discharge": ["malodorous vaginal discharge", "foul-smelling secretions", "bad smelling discharge"],
    "burning sensation in peeing": ["painful urination", "discomfort while urinating"],
    "anal itching": ["itchiness around the anus", "rectal itching"],
    "bloody urine": ["blood in urine", "hematuria"],
    "lower abdomen pressure": ["feeling of pressure in the lower abdomen", "abdominal heaviness"],
    "lower abdomen cramping": ["abdominal cramps", "stomach discomfort"],
    "burning sensation when peeing": ["burning", "burns when pee"]
}



# Load symptoms from CSV
def load_symptoms(csv_filepath='symptoms.csv'):
    symptoms_list = []
    # Open csv to read
    with open('symptoms.csv', mode='r') as csvfile:
        reader = csv.DictReader(csvfile) 

        for row in reader:
            symptoms = row['Symptoms'].split(', ') 
            for symptom in symptoms:
                # Check if the symptom is a qualifier
                if symptom.lower() in qualifiers:
                    symptoms_list.extend(qualifiers[symptom.lower()])
                # Add the symptom to the list
                if symptom not in symptoms_list:
                    symptoms_list.append(symptom)

    return symptoms_list

symptoms_list = load_symptoms()
model = SentenceTransformer('all-MiniLM-L6-v2')
symptomEmbedding = model.encode(symptoms_list, convert_to_tensor=True)
iknow = iknowpy.iKnowEngine()

def getSymptomList(userInput, top_n=2, threshold = 0.2):
    stemmer = PorterStemmer()
    iknow.index(userInput, "en")
    paragraph = []

    for s in iknow.m_index['sentences']:
        for e in s['entities']:
            if e['type'] in ['Concept', 'Relation']:
                paragraph.append(e['index'])

    words = [stemmer.stem(word) for word in paragraph]
    userSentence = ' '.join(words)

    patientResponse = [userSentence]
    patientEmbedding = model.encode(patientResponse, convert_to_tensor=True)
    cosine_scores = util.cos_sim(patientEmbedding, symptomEmbedding)

    # Rank symptoms by similarity score
    ranked_symptoms = sorted(zip(symptoms_list, cosine_scores[0]), key=lambda x: x[1], reverse=True)

    # Select top N symptoms based on similarity
    top_symptoms = [symptom for symptom, score in ranked_symptoms[:top_n]]
    return top_symptoms
