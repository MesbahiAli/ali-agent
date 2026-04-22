import pyttsx3
import json
import random
from datetime import datetime

# === Load data ===
with open('./data.json') as file:
    data = json.load(file)

with open('./quotes.json') as file:
    quotes = json.load(file)

streak = data["streak"]
today_quote = random.choice(quotes)

# === Setup voice ===
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('rate', 175)
engine.setProperty('voice', voices[1].id)

# === Dates ===
today_display = datetime.today().strftime("%A, %B %d, %Y")
today_compare = datetime.today().strftime("%Y-%m-%d")

# === Greeting ===
greeting = f"Hello Mr Ali, today is {today_display}. You are currently on a {streak} day streak."
print(greeting)
engine.say(greeting)

# === Motivation quote ===
quote_message = f"Ali, your quote for today is. {today_quote}"
print(quote_message)
engine.say(quote_message)

# === Daily check-in ===

question_text = "Did you complete your coding session today?"
engine.say(question_text)
engine.runAndWait()

answer = input("Type y or n: ").lower()

if answer == "y":
    if today_compare != data["last_date"]:
        data["streak"] += 1
        data["last_date"] = today_compare
        with open('./data.json', 'w') as file:
            json.dump(data, file)
        final_message = f"Amazing! Streak updated to {data['streak']} days. See you tomorrow Ali."
    else:
        final_message = "You already confirmed today. Rest well."
elif answer == "n":
    final_message = "No problem. Rest is part of the journey. See you tomorrow."
else:
    final_message = "Please answer with y or n next time."

print(final_message)
engine.say(final_message)
engine.runAndWait()