import pyttsx3
import json
from datetime import datetime

# Load user data
with open('./data.json') as file:
    data = json.load(file)

streak = data["streak"]

# Setup voice engine
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('rate', 175)
engine.setProperty('voice', voices[1].id)

# Get today's date for display
today = datetime.today().strftime("%A, %B %d, %Y")

# Greeting
greeting = f"Hello Mr Ali, today is {today}. You are currently on a {streak} day streak. Keep going."
print(greeting)
engine.say(greeting)
engine.runAndWait()

# Ask the user
answer = input("Did you code today? (y/n): ").lower()

# Get today as comparable string
today_string = datetime.today().strftime("%Y-%m-%d")

# Handle answer
if answer == "y":
    if today_string != data["last_date"]:
        data["streak"] += 1
        data["last_date"] = today_string
        
        with open('./data.json', 'w') as file:
            json.dump(data, file)
        
        new_streak = data["streak"]
        final_message = f"Amazing! Streak updated to {new_streak} days. See you tomorrow Ali."
    else:
        final_message = "You already confirmed today. Rest well."
elif answer == "n":
    final_message = "No problem. Rest is part of the journey. See you tomorrow."
else:
    final_message = "Please answer with y or n next time."

# Speak final
print(final_message)
engine.say(final_message)
engine.runAndWait()