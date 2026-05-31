import time
from datetime import datetime

def type_effect(text):
    for char in text:
        print(char, end="", flush=True)
        time.sleep(0.03)
    print()

def get_timestamp():
    return datetime.now().strftime("%H:%M:%S")

def welcome_screen():
    print()
    print("╔══════════════════════════════════════════════╗")
    print("║       DecoBot AI — DecodeLabs 2026           ║")
    print("║       Rule-Based Intelligence Engine         ║")
    print("║       Batch 2026 | Powered by DecodeLabs     ║")
    print("╚══════════════════════════════════════════════╝")
    print()
    type_effect("  Initializing DecoBot...")
    time.sleep(0.5)
    type_effect("  Loading Knowledge Base...")
    time.sleep(0.5)
    type_effect("  All Systems Operational! ✅")
    time.sleep(0.5)
    print()
    print("  Type 'help' to see what I can do.")
    print("  Type 'exit' to quit.")
    print()
    print("─" * 48)
    print()

# Memory storage
memory = {}

# The brain of the chatbot
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
    "help": "Try: hello, how are you, what is ai, what is ml, tell me a joke, tell me a fact, my name is ...",
}

def get_response(clean_input):
    # memory - remember name
    if "my name is" in clean_input:
        name = clean_input.replace("my name is", "").strip().title()
        memory["name"] = name
        return f"Nice to meet you {name}! I'll remember that 😊"

    # memory - recall name
    if "what is my name" in clean_input or "my name" == clean_input:
        if "name" in memory:
            return f"Your name is {memory['name']}!"
        return "I don't know your name yet! Tell me with 'my name is ...'"

    # memory - remember age
    if "my age is" in clean_input:
        age = clean_input.replace("my age is", "").strip()
        memory["age"] = age
        return f"Got it! You are {age} years old 👍"

    # memory - recall age
    if "what is my age" in clean_input:
        if "age" in memory:
            return f"You are {memory['age']} years old!"
        return "I don't know your age yet! Tell me with 'my age is ...'"

    # greeting with name like "hi i'm hansika"
    if "hi" in clean_input or "hello" in clean_input:
        if "i'm" in clean_input or "im" in clean_input or "i am" in clean_input:
            # extract name after i'm/im/i am
            for word in ["i'm", "im", "i am"]:
                if word in clean_input:
                    name = clean_input.split(word)[-1].strip().title()
                    memory["name"] = name
                    return f"Hey {name}! Great to meet you 😊"

    # dictionary lookup
    return responses.get(clean_input, "I don't understand that yet! Type 'help' to see what I can do.")

# Show welcome screen
welcome_screen()

while True:
    raw_input = input("You: ")
    clean_input = raw_input.lower().strip()
    timestamp = get_timestamp()

    # exit
    if clean_input in ["exit", "quit", "stop"]:
        print(f"[{timestamp}]")
        type_effect("DecoBot: Shutting down. Goodbye! 👋")
        break

    # empty input
    if clean_input == "":
        type_effect("DecoBot: Please type something!")
        continue

    # get response
    response = get_response(clean_input)
    print(f"[{timestamp}]")
    type_effect("DecoBot: " + response)