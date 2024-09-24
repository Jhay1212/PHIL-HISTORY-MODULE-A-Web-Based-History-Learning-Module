import os

os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'

import random
import json
import pickle
import numpy as np

import nltk
from nltk.stem import WordNetLemmatizer

from tensorflow.keras.models import load_model


def clean_up_sentence(sentence):
    lemmatizer = WordNetLemmatizer()

    sentence_words = nltk.word_tokenize(sentence)
    sentence_words = [lemmatizer.lemmatize(word) for word in sentence_words]

    return sentence_words


def bag_of_words(sentence):
    words = pickle.load(open(r'C:\Users\Jhay\projects\thesis\words.pkl', 'rb'))

    sentence_words = clean_up_sentence(sentence)
    bag = [0] * len(words)
    for w in sentence_words:
        for i, word in enumerate(words):
            if word == w:
                bag[i] = 1
    return np.array(bag)


def predict_class(sentence):
    classes = pickle.load(open(r'C:\Users\Jhay\projects\thesis\classes.pkl', 'rb'))
    model = load_model(r'C:\Users\Jhay\projects\thesis\history\chatbot\chatbot_model.keras')

    bow = bag_of_words(sentence)
    res = model.predict(np.array([bow]))[0]
    ERROR_THRESHOLD = 0.25

    results = [[i, r] for i, r in enumerate(res) if r > ERROR_THRESHOLD]
    results.sort(key=lambda x: x[1], reverse=True)

    return_list = []

    for r in results:
        return_list.append({'intent': classes[r[0]], 'probability': str(r[1])})

    return return_list


def get_response(intents_list):
    intents_json = json.load(open(r'C:\Users\Jhay\projects\thesis\history\chatbot\intent.json'))

    tag = intents_list[0]['intent']
    list_of_intents = intents_json['intents']

    for i in list_of_intents:
        if i['tag'] == tag:
            result = random.choice(i['responses'])
            break

    return result










# import json 
# from difflib import get_close_matches

# def load_data(filename: str) -> dict:
#     with open(filename, 'r') as file:
#         data = file.read()

#     return data

# def save_data(data: dict, filename: str)  -> None:
#     with open(filename, 'w') as file:
#         json.dumps(data, filename, indent=4)

    

# def find_save_matches(user_question: str, question: list[str]) -> str | None:
#     matches: list = get_close_matches(user_question, question, n=1, cutoff=.8)
#     return matches if matches else None

# def get_answer_for_question(question: str, data_pool: dict) -> str:
#     for q in data_pool['questions']:
#         if q['question'] == question:
#             return q['answer']
        

# def chatbot():
#     knowledge_base = load_data('data.json')
#     question = input('Enter a question: ').lower()

#     best_match = find_save_matches(question=question, data_pool=[q['question'] for q in knowledge_base['questions']])
#     if best_match:
#         print(best_match)
#     else:
#         None


# if __name__ == '__main__':
#     chatbot()