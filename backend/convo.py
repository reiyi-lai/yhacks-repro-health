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
