import random
from tensorflow.python.keras.optimizers import SGD
from tensorflow.python. keras import Dense, Dropout
from tensorflow.python.keras.models import load_model
from tensorflow.python.keras.models import Sequential
import numpy as np
import pickle
import json
import nltk
from flask.blueprints import Blueprint
from flask import render_template, request
from nltk.stem import WordNetLemmatizer as lemmatizer
# from tensorflow.python.l
nltk.download('omw-1.4')
nltk.download("punkt")
nltk.download("wordnet")

words = []
classes = []
documents = []
ignored_words = ['?', '!']
data_file = open('intents.json').read()
intents = json.load(data_file)

for intent in intents:
    for pattern in intent['pattern']:
        w = nltk.word_tokenize(pattern)
        words.extend(w)
        documents.append((words, intent['tag']))

        if intent['tag'] not in classes:
            classes.append(intent['tag'])

words = [lemmatizer.lemmatize(w.lower() for w in words if w not in ignored_words)]
words = sorted(list(set(words)))
classes = sorted(list(set(classes)))

pickle.dump(words, open('words.pkl', 'wb'))
pickle.dump(classes, open('classes.pkl', 'wb'))

training = []
empty_output = [0] * len(classes)

for doc in documents:
    bag = []
    pattern = doc[0]
    pattern_words = [lemmatizer.lemmatize(word.lower()) for word in pattern_words]
    for w in words:
        bag.append(1) if w in pattern_words else bag.append(0)

    output_row = list(empty_output)
    output_row[classes.index(doc[1])] = 1
    training.append([bag, output_row])

random.shuffle(training)
training = np.array(training)
train_x = list(training[:, 0])
training_y = list(training[:, 1])
print('done training')

model = Sequential()
model.add(Dense(128, input_shape=(len(train_x, ), ), activation='relu'))
model.add(Dropout(0.5))
model.add(Dense(64, activation='relu'))
model.add(Dropout(0.5))
model.add(Dense(len(training_y), activation='softmax'))
model.summary()

sgd = SGD(lr=0.01, decay=1e-6, momentum=0.9, nesterov=True)
model.compile(loss='categorical_crossentropy', optimizer=sgd, metrics=['accuracy'])

from tensorflow.python.keras.callbacks import EarlyStopping, ModelCheckpoint
early_stopping = EarlyStopping(monitor='loss', mode='min', patience=5, restore_best_weights=True)
callbacks = [early_stopping]

hist = model.fit(np.array(train_x), np.array(training_y), epochs=200, batch_size=5, verbose=1)
model.save("chatbot_model.h5", hist)
print('model created')

from flask import Blueprint, render_template, redirect, url_for, request

cbot = Blueprint('chatbot', __name__, template_folder='templates')

@cbot.route('/chatbot')
def main():
    return render_template('main.html')

# @cbot.route('/get', methods=['POST'])
# def chatbot_response():
#     msg = request.args.get('msg')
#     if msg.startswith('my name is'):
#         name = msg[11:]
#         ints = model.predict()
#         res1 = getResponse(ints, intents)
#         res =res1.replace("{n}",name)
#     elif msg.startswith('hi my name is'):
#         name = msg[14:]
#         ints = predict_class(msg, model)
#         res1 = getResponse(ints, intents)
#         res =res1.replace("{n}",name)
#     else:
#         ints = predict_class(msg, model)
#         res = getResponse(ints, intents)
#     return res