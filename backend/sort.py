import csv

symptomsList = []
diseasesList = []
dsMap = {} #disease symptoms map


#open csv to read
with open('./data/symptoms.csv', mode='r') as csvfile:
        reader = csv.DictReader(csvfile) 

        for row in reader:
                diseasesList.append(row['Disease Name'])
                symptoms = row['Symptoms'].split(', ') #splits symptoms by commas
                for symptom in symptoms:
                    if symptom not in symptomsList:  # dupe check
                        symptomsList.append(symptom)
                        dsMap[row['Disease Name']] = symptoms
                        
def identify_potential_diseases(initialSymptom):
    potentialDiseases = []
    for disease, symptoms in dsMap.items():
        if initialSymptom in symptoms:
            potentialDiseases.append(disease)
            print("potentialDiseases", potentialDiseases)

    return potentialDiseases



#print("Diseases:", diseasesList)
#print("Symptoms List:", symptomsList)

