#!/usr/bin/env python
# coding: utf-8

# In[7]:


import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords

nltk.download('punkt')
nltk.download('stopwords')

disease_symptoms = {
    "flu": ["fever", "cough", "sore throat", "fatigue"],
    "cold": ["sneezing", "runny nose", "cough", "sore throat"],
    "covid": ["fever", "cough", "loss of taste", "shortness of breath"],
    "malaria": ["fever", "chills", "sweating", "headache"]
}

def diagnose(symptoms):
    symptoms = set(symptoms)
    possible_diseases = {}
    
    for disease, disease_sym in disease_symptoms.items():
        match_count = len(set(disease_sym) & symptoms)
        if match_count:
            possible_diseases[disease] = match_count
    
    if not possible_diseases:
        return "No clear diagnosis. Please consult a doctor."
    
    return max(possible_diseases, key=possible_diseases.get)

def main():
    user_input = input("Enter your symptoms separated by commas: ")
    tokens = word_tokenize(user_input.lower())
    filtered_tokens = [word for word in tokens if word.isalpha() and word not in stopwords.words('english')]
    
    diagnosis = diagnose(filtered_tokens)
    print("Possible diagnosis:", diagnosis)

if __name__ == "__main__":
    main()


# In[ ]:





# In[ ]:




