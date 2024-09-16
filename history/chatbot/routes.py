from flask import Blueprint, render_template, redirect, url_for, request
from flask import Flask, request, jsonify
import numpy as np
import tensorflow as tf
import json
import random
import nltk
from nltk.stem import WordNetLemmatizer
import pickle

from .forms import Chatbot

import os 


directory = os.path.dirname(os.path.abspath(__file__))
lemmatizer = WordNetLemmatizer()
model = tf.keras.models.load_model('chatbot_model.h5')
words_path = os.path.join(directory, 'static', 'words.pkl')
classes_path = os.path.join(directory, 'static', 'classes.pkl')
# Load data structures
words = pickle.load(open('words.pkl', 'rb'))
classes = pickle.load(open('classes.pkl', 'rb'))
intents = json.loads(open(os.path.join('static', 'chatbot', 'intent.json')).read())

# Tokenize input and create bag of words
def clean_up_sentence(sentence):
    sentence_words = nltk.word_tokenize(sentence)
    sentence_words = [lemmatizer.lemmatize(word.lower()) for word in sentence_words]
    return sentence_words

def bag_of_words(sentence, words):
    sentence_words = clean_up_sentence(sentence)
    bag = [0] * len(words)
    for s in sentence_words:
        for i, word in enumerate(words):
            if word == s:
                bag[i] = 1
    return np.array(bag)

def predict_class(sentence, model):
    bow = bag_of_words(sentence, words)
    res = model.predict(np.array([bow]))[0]
    ERROR_THRESHOLD = 0.25
    results = [[i, r] for i, r in enumerate(res) if r > ERROR_THRESHOLD]

    results.sort(key=lambda x: x[1], reverse=True)
    return_list = []
    for r in results:
        return_list.append({'intent': classes[r[0]], 'probability': str(r[1])})
    return return_list

def get_response(intents_list, intents_json):
    tag = intents_list[0]['intent']
    for i in intents_json['intents']:
        if i['tag'] == tag:
            return random.choice(i['responses'])



# from . import train
cbot = Blueprint('chatbot', __name__, template_folder='templates')

@cbot.route('/chatbot')
def main():
    return render_template('main.html')

@cbot.route('/get', methods=['POST'])
def chatbot_response():
    # msg = 
    pass 

@cbot.route('/chat0', methods=['POST', 'GET'])
def chat():
    forms = Chatbot()
    if forms.validate_on_submit():

        data = request.get_json()
        message = data['message']
        intents_list = predict_class(message, model)
        response = get_response(intents_list, intents)
        return jsonify({'response': response})
    return render_template('chat.html', forms=forms)

print(cbot.static_url_path)