import random
import json
import pickle
import numpy as np
import tensorflow as tf
import nltk
from nltk.stem import WordNetLemmatizer

# Download required NLTK data (run once)
nltk.download('punkt_tab')
nltk.download('wordnet')

lemmatizer = WordNetLemmatizer()
intents = json.loads(open('intents.json').read())

words = []
classes = []
documents = []  # fixed typo (was: documwnts)
ignore_letters = ['?', '!', '.', ',']

for intent in intents['intents']:  # fixed syntax (was: intents ['intents'])
    for pattern in intent['patterns']:
        word_list = nltk.word_tokenize(pattern)
        words.extend(word_list)
        documents.append((word_list, intent['tag']))
        if intent['tag'] not in classes:
            classes.append(intent['tag'])

words = [lemmatizer.lemmatize(w.lower()) for w in words if w not in ignore_letters]
words = sorted(set(words))  # fixed typo (was: set(classes))

classes = sorted(set(classes))

pickle.dump(words, open('words.pkl', 'wb'))
pickle.dump(classes, open('classes.pkl', 'wb'))

training = []
output_empty = [0] * len(classes)

for document in documents:
    bag = []
    word_patterns = document[0]
    word_patterns = [lemmatizer.lemmatize(w.lower()) for w in word_patterns]
    for w in words:
        bag.append(1 if w in word_patterns else 0)

    output_row = list(output_empty)
    output_row[classes.index(document[1])] = 1
    training.append(bag + output_row)

random.shuffle(training)
training = np.array(training)

train_x = training[:, :len(words)]  # fixed typo (was: lan(words))
train_y = training[:, len(words):]

# Create the model
model = tf.keras.Sequential()  # fixed typo (was: sequentiol)

model.add(tf.keras.layers.Dense(128, input_shape=(len(train_x[0]),), activation='relu'))
model.add(tf.keras.layers.Dropout(0.5))
model.add(tf.keras.layers.Dense(64, activation='relu'))
model.add(tf.keras.layers.Dense(len(train_y[0]), activation='softmax'))  # fixed: trainy -> train_y

# Optimizer
sgd = tf.keras.optimizers.SGD(learning_rate=0.01, momentum=0.9, nesterov=True)

model.compile(loss='categorical_crossentropy', optimizer=sgd, metrics=['accuracy'])

# Fit the model
hist = model.fit(train_x, train_y, epochs=200, batch_size=5, verbose=1)

# Save model and history
model.save('chatbot_model.h5')
print("Training completed and model saved.")
