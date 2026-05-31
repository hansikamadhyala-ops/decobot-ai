from flask import Flask, request, jsonify, render_template
from datetime import datetime
from history import save_message, load_history
from groq import Groq
from dotenv import load_dotenv
import os

# Load API key from .env
load_dotenv()

app = Flask(__name__)

# Groq client
client = Groq(api_key=os.environ.get("GROQ_API_KEY"))

# Memory storage
memory = {}

# Rule-Based Knowledge Base
responses = {
    "hello": "Hey there! How can I help you?",
    "hi": "Hi! What's on your mind?",
    "how are you": "I'm running perfectly! How about you?",
    "what is ai": "AI is the simulation of human intelligence by machines.",
    "what is ml": "ML is a subset of AI where machines learn from data!",
    "what is python": "Python is the most popular language for AI development!",
    "bye": "Goodbye! Keep building great things!",
    "who are you": "I'm DecoBot, a rule-based AI built at DecodeLabs!",
    "what can you do": "I can answer your questions using rule-based logic!",
    "tell me a joke": "Why do programmers prefer dark mode? Light attracts bugs! 🐛",
    "tell me a fact": "The first chatbot ELIZA was built in 1966 at MIT!",
    "what is a chatbot": "A chatbot is a program that simulates conversation — like me!",
    "what is deep learning": "Deep Learning is a subset of ML that uses neural networks!",
    "what is flask": "Flask is a lightweight Python web framework!",
    "what is an api": "An API is a bridge that lets two applications talk to each other!",
    "help": "Try: hello, who are you, what is ai, what is ml, tell me a joke, my name is ...",
}

def get_ai_response(user_message):
    """Fallback to Groq AI when no rule matches"""
    try:
        chat_completion = client.chat.completions.create(
            messages=[
                {
                    "role": "system",
                    "content": "You are DecoBot, a helpful AI assistant built at DecodeLabs. Keep responses short, friendly and concise — max 2-3 sentences."
                },
                {
                    "role": "user",
                    "content": user_message
                }
            ],
            model="llama-3.3-70b-versatile",
        )
        return chat_completion.choices[0].message.content
    except Exception as e:
        print("GROQ ERROR:", str(e))
        return "I'm having trouble connecting to my AI brain right now. Try again!"

def get_response(clean_input, original_input):
    # Memory - remember name
    if "my name is" in clean_input:
        name = clean_input.replace("my name is", "").strip().title()
        memory["name"] = name
        return f"Nice to meet you {name}! I'll remember that 😊", "rule"

    # Memory - recall name
    if "what is my name" in clean_input or clean_input == "my name":
        if "name" in memory:
            return f"Your name is {memory['name']}!", "rule"
        return "I don't know your name yet! Tell me with 'my name is ...'", "rule"

    # Memory - remember age
    if "my age is" in clean_input:
        age = clean_input.replace("my age is", "").strip()
        memory["age"] = age
        return f"Got it! You are {age} years old 👍", "rule"

    # Memory - recall age
    if "what is my age" in clean_input:
        if "age" in memory:
            return f"You are {memory['age']} years old!", "rule"
        return "I don't know your age yet! Tell me with 'my age is ...'", "rule"

    # Greeting with name
    if "hi" in clean_input or "hello" in clean_input:
        if "i'm" in clean_input or "im" in clean_input or "i am" in clean_input:
            for word in ["i'm", "im", "i am"]:
                if word in clean_input:
                    name = clean_input.split(word)[-1].strip().title()
                    memory["name"] = name
                    return f"Hey {name}! Great to meet you 😊", "rule"

    # Dictionary lookup
    if clean_input in responses:
        return responses[clean_input], "rule"

    # Hybrid Architecture
    # No rule matched → pass to Groq AI
    ai_response = get_ai_response(original_input)
    return ai_response, "ai"

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    user_message = request.json.get("message", "")
    clean_input = user_message.lower().strip()
    timestamp = datetime.now().strftime("%H:%M:%S")

    # Save user message
    save_message("user", user_message)

    response, source = get_response(clean_input, user_message)

    # Save bot response
    save_message("bot", response, source)

    return jsonify({
        "response": response,
        "timestamp": timestamp,
        "source": source
    })

@app.route("/history", methods=["GET"])
def get_history():
    """Endpoint to view full chat history"""
    return jsonify(load_history())

if __name__ == "__main__":
    app.run(debug=True)