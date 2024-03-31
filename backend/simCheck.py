 #checks similarity of user input with symptoms list
#import nltk
from nltk.stem import PorterStemmer
import iknowpy
from sentence_transformers import SentenceTransformer, util

#nltk.download()

# initialize the engine
iknow = iknowpy.iKnowEngine()

symptoms_list = [
    "Blisters on the rectum",
    "Blisters around the rectum",
    "Blisters on the mouth",
    "Blisters around the mouth",
    "Blisters outside vagina",
    "Blisters inside vagina",
    "Thin vaginal discharge",
    "White vaginal discharge",
    "Gray vaginal discharge",
    "Increased vaginal discharge",
    "Rectal pain",
    "Pain in vagina",
    "Itching in vagina",
    "Burning in vagina",
    "Burning when peeing",
    "Fish-like odor",
    "Itching around outside of vagina",
    "Painful periods",
    "Debilitating periods",
    "Vaginal bleeding between periods",
    "Pain during sex",
    "Pain in intestine",
    "Pain in lower abdomen",
    "Painful bowel movements",
    "Heavy menstrual periods",
    "Premenstrual spotting",
    "Infertility",
    "Miscarriages",
    "Fever",
    "Chills",
    "Night sweats",
    "Muscle aches",
    "Sore throat",
    "Fatigue",
    "Swollen lymph nodes",
    "Mouth ulcers",
    "Rapid weight loss",
    "Recurring fever",
    "Extreme fatigue",
    "Prolonged swelling of lymph glands",
    "Diarrhea (over a week)",
    "Pneumonia",
    "Memory loss",
    "Abdominal discomfort",
    "Abdominal pressure",
    "Pelvic discomfort",
    "Pelvic pressure",
    "Frequent urination",
    "Tenderness",
    "Pain in pelvic region",
    "Feeling of urgency to urinate"
]

# compute the embeddings of the symptoms_list
model = SentenceTransformer('all-MiniLM-L6-v2')
symptomEmbedding = model.encode(symptoms_list, convert_to_tensor=True)


def getSymptomList(userInput):

    stemmer = PorterStemmer()

    iknow.index(userInput, "en")
    paragraph=[]

    # parse the patient input to only include concepts or relations  
    for s in iknow.m_index['sentences']:
        for e in s['entities']:
            if(e['type']=='Concept' or e['type']=='Relation'):
                paragraph.append(e['index'])

    words = [stemmer.stem(word) for word in paragraph]

    userSentence = ' '.join(words)
    print(userSentence)

    patientResponse = [userSentence]

    # compute the embeddings of both 
    patientEmbedding = model.encode(patientResponse, convert_to_tensor=True)

    #Compute cosine-similarities
    cosine_scores = util.cos_sim(patientEmbedding, symptomEmbedding)

    #Output the pairs with their score
    scores = dict()
    for i in range(len(symptoms_list)):
        scores[symptoms_list[i]] = cosine_scores[0][i]
    
    scores = sorted(scores.items(), reverse=True, key=lambda x:x[1])
    print("Similar symptom calculated: " + str(scores[0][0]))

    #only return most relevant symptom as string
    return scores[0][0]


# test different user inputs:
getSymptomList("I have pain when I pee")
print("\n")

getSymptomList("My stomach hurts")