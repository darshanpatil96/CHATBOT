from flask import Flask, render_template, request, jsonify
import chatbot   # imports get_response() from chatbot.py
import webbrowser
import os

app = Flask(__name__)

# Route for frontend
@app.route("/")
def index():
    return render_template("index.html")   # loads templates/index.html

# API endpoint for chatbot responses
@app.route("/get", methods=["POST"])
def get_bot_response():
    user_message = request.json.get("message", "").strip()

    if not user_message:
        return jsonify({"response": "⚠️ Please enter a message."})

    # Call the get_response function from chatbot.py
    bot_reply = chatbot.get_response(user_message)
    return jsonify({"response": bot_reply})


if __name__ == "__main__":
    # For Heroku or production: bind to 0.0.0.0 with dynamic port
    port = int(os.environ.get("PORT", 5000))
    
    # If running locally, auto-open browser
    if port == 5000:
        webbrowser.open("http://127.0.0.1:5000/")

    app.run(host="0.0.0.0", port=port, debug=True)
