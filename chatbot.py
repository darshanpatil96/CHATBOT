import random
import json
import pickle
import numpy as np
from keras.models import load_model
from nltk.stem import WordNetLemmatizer
from nltk.tokenize import word_tokenize

# Initialize tools
lemmatizer = WordNetLemmatizer()

# Load intents and model data
intents = json.loads(open('intents.json').read())
words = pickle.load(open('words.pkl', 'rb'))
classes = pickle.load(open('classes.pkl', 'rb'))
model = load_model('chatbot_model.h5')


def clean_up_sentence(sentence):
    """Tokenize and lemmatize the input sentence."""
    sentence_words = word_tokenize(sentence)
    sentence_words = [lemmatizer.lemmatize(word.lower()) for word in sentence_words]
    return sentence_words


def bow(sentence, words):
    """Convert a sentence into a bag-of-words array."""
    sentence_words = clean_up_sentence(sentence)
    bag = [0] * len(words)
    for s in sentence_words:
        for i, w in enumerate(words):
            if w == s:
                bag[i] = 1
    return np.array(bag)


def predict_class(sentence):
    """Predict the intent class of a given sentence."""
    p = bow(sentence, words)
    res = model.predict(np.array([p]))[0]
    ERROR_THRESHOLD = 0.25
    results = [[i, r] for i, r in enumerate(res) if r > ERROR_THRESHOLD]

    results.sort(key=lambda x: x[1], reverse=True)
    return_list = []
    for r in results:
        return_list.append({"intent": classes[r[0]], "probability": str(r[1])})
    return return_list


def get_response(msg):
    """Main function: take user message and return chatbot reply."""
    ints = predict_class(msg)

    if len(ints) == 0:
        return "🤔 I'm not sure what you mean. Could you rephrase?"

    tag = ints[0]['intent']
    for intent in intents['intents']:
        if intent['tag'] == tag:
            return random.choice(intent['responses'])

    return "Sorry, I didn't get that."
