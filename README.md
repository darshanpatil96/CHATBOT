# CHATBOT
An AI-powered chatbot built with Flask and TensorFlow/Keras. It uses a trained deep learning model (chatbot_model.h5) to classify intents from user messages and respond accordingly. The project includes a frontend (HTML, CSS, JS) for a clean chat interface and is deployment-ready with a Procfile and requirements.txt.

✨ Features
Web-based Interface: Simple and clean UI for easy interaction.

Natural Language Understanding: Uses a deep learning model to understand user intent.

Easily Extendable: New intents and responses can be added by simply modifying the intents.json file.

Ready for Deployment: Includes a Procfile for easy deployment to platforms like Heroku.

💻 Technology Stack
Backend: Python, Flask

Machine Learning: TensorFlow, Keras

NLP Toolkit: NLTK (likely used for text preprocessing)

Frontend: HTML, CSS, JavaScript (served from the static and templates folders)

📂 File Structure
Here is an overview of the key files and directories in the project:

├── static/              # Contains static assets (CSS, JavaScript, images)
├── templates/           # Contains HTML templates for the web interface
├── __pycache__/         # Python cache directory
├── app.py               # The main Flask application file that runs the web server
├── chatbot.py           # Contains the core chatbot logic for processing input and getting predictions
├── chatbot_model.h5     # The pre-trained Keras sequential model for intent classification
├── classes.pkl          # A pickled file containing the list of intent classes
├── words.pkl            # A pickled file containing the vocabulary of the model
├── intents.json         # The dataset file with predefined intents, patterns, and responses
├── new.py               # (Assumed) The script used to train the neural network model
├── requirements.txt     # A list of all Python dependencies for the project
├── Procfile             # Configuration file for deployment platforms like Heroku
└── README.md            # This README file


Of course! Based on the file structure in the image, here is a comprehensive README.md file for your project. This README explains what the project is, what the files do, and how to run it.

AI Chatbot with Flask
This is a web-based AI Chatbot application built using Python, Flask, and a deep learning model created with Keras/TensorFlow. The chatbot is designed to understand user queries and provide relevant responses based on a predefined set of intents.

📋 Table of Contents
Project Overview

Features

Technology Stack

File Structure

Setup and Installation

How It Works

Usage

📝 Project Overview
This project implements a simple, intent-based chatbot with a web interface. The core of the chatbot is a neural network model that classifies user input into different categories (intents). The Flask web application serves an HTML interface for users to interact with the chatbot in real-time.

✨ Features
Web-based Interface: Simple and clean UI for easy interaction.

Natural Language Understanding: Uses a deep learning model to understand user intent.

Easily Extendable: New intents and responses can be added by simply modifying the intents.json file.

Ready for Deployment: Includes a Procfile for easy deployment to platforms like Heroku.

💻 Technology Stack
Backend: Python, Flask

Machine Learning: TensorFlow, Keras

NLP Toolkit: NLTK (likely used for text preprocessing)

Frontend: HTML, CSS, JavaScript (served from the static and templates folders)

📂 File Structure
Here is an overview of the key files and directories in the project:

├── static/              # Contains static assets (CSS, JavaScript, images)
├── templates/           # Contains HTML templates for the web interface
├── __pycache__/         # Python cache directory
├── app.py               # The main Flask application file that runs the web server
├── chatbot.py           # Contains the core chatbot logic for processing input and getting predictions
├── chatbot_model.h5     # The pre-trained Keras sequential model for intent classification
├── classes.pkl          # A pickled file containing the list of intent classes
├── words.pkl            # A pickled file containing the vocabulary of the model
├── intents.json         # The dataset file with predefined intents, patterns, and responses
├── new.py               # (Assumed) The script used to train the neural network model
├── requirements.txt     # A list of all Python dependencies for the project
├── Procfile             # Configuration file for deployment platforms like Heroku
└── README.md            # This README file

📷 Screenshot
<img width="536" height="616" alt="Screenshot 2025-09-12 173908" src="https://github.com/user-attachments/assets/4814de02-7dce-4f46-a2f4-f02fba19ffd3" />



⚙️ Setup and Installation
To run this project locally, follow these steps:

1. Prerequisites:

Python 3.7+

pip package manager

2. Clone the Repository:

Bash

git clone <your-repository-url>
cd <repository-directory>
3. Create and Activate a Virtual Environment (Recommended):

For macOS/Linux:

Bash

python3 -m venv venv
source venv/bin/activate
For Windows:

Bash

python -m venv venv
.\venv\Scripts\activate
4. Install Dependencies:
Install all the required Python packages from the requirements.txt file.

Bash

pip install -r requirements.txt
5. Run the Application:
Start the Flask development server.

Bash

python app.py
6. Access the Chatbot:
Open your web browser and navigate to:
http://127.0.0.1:5000

🧠 How It Works
Training (using new.py):

The intents.json file is read, which contains tags (intents), patterns (example user phrases), and responses.

The text patterns are preprocessed (tokenized, lemmatized, etc.).

A vocabulary (words.pkl) and a list of classes/intents (classes.pkl) are created and saved.

A "bag of words" representation is created from the processed text data.

A sequential neural network is built and trained on this data.

The trained model is saved as chatbot_model.h5.

Inference (in app.py and chatbot.py):

The Flask application (app.py) serves the web interface and handles user requests.

When a user sends a message, it is sent to the Flask backend.

The backend preprocesses the user's message in the same way as the training data.

The trained model (chatbot_model.h5) is used to predict the intent of the message.

Based on the predicted intent, a random response is selected from the list of appropriate responses in intents.json.

The selected response is sent back to the web interface and displayed to the user.
