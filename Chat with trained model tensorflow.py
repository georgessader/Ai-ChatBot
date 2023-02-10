import nltk
from nltk.stem.lancaster import LancasterStemmer
import numpy as np
import tflearn
import json
import pickle
import random
import os

lang="arb"
#Loading intents.json
if lang=="arb":
    with open('intentsaren.json', encoding='utf-8-sig') as intents:
        data = json.load(intents)
else:
    with open('old example.json') as intents:
        data = json.load(intents)

stemmer = LancasterStemmer()

if os.path.exists("data.pickle"):
    with open('data.pickle','rb') as f:
        words, labels, training, output = pickle.load(f)
else:
    print("Please train the model and save it1")


net = tflearn.input_data(shape=[None, len(training[0])])
net = tflearn.fully_connected(net, 8)
net = tflearn.fully_connected(net, 8)
net = tflearn.fully_connected(net, len(output[0]), activation='softmax')
net = tflearn.regression(net)

model = tflearn.DNN(net)

if os.path.exists("model.tflearn.index"):
    model.load("model.tflearn")
else:
    print("Please train the model and save it2")


def bag_of_words(s, words):
    s_words=""
    bag=[]
    w=""
    bag = [0 for _ in range(len(words))]
    s_words = nltk.word_tokenize(s)
    s_words = [stemmer.stem(word.lower()) for word in s_words]

    for se in s_words:
        for i, w in enumerate(words):
            if w == se:
                bag[i] = 1

    return np.array(bag)


def chat():
    print("The bot is ready to talk!!(Type 'quit' to exit)")
    while True:
        responses = "Cannot find the answear"
        inp = input("\nYou: ")
        if inp.lower() == 'quit':
            break

    #Porbability of correct response 
        results = model.predict([bag_of_words(inp, words)])

    # Picking the greatest number from probability
        results_index = np.argmax(results)

        tag = labels[results_index]


        for tg in data['intents']:

            if tg['tag'] == tag:
                responses = tg['responses']
        print("Bot:" + str(tag))
chat()