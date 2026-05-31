import json
import os
from datetime import datetime

HISTORY_FILE = "chat_history.json"

def load_history():
    """Load existing chat history from file"""
    if os.path.exists(HISTORY_FILE):
        with open(HISTORY_FILE, "r") as f:
            return json.load(f)
    return []

def save_message(role, message, source=None):
    """Save a single message to history"""
    history = load_history()
    history.append({
        "role": role,
        "message": message,
        "source": source,
        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    })
    with open(HISTORY_FILE, "w") as f:
        json.dump(history, f, indent=2)