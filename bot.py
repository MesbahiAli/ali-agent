from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes
import json
from datetime import datetime
from dotenv import load_dotenv

import os


today_compare = datetime.now().strftime("%d/%m/%Y")

with open("data.json","r") as file:
    global data
    data=json.load(file)

load_dotenv()
TOKEN = os.getenv("TELEGRAM_TOKEN")


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Hello! I'm DevPulse — your coding accountability agent! 🚀")


async def streak(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(f"🔥 You are on a {data['streak']} day streak!\n📅 Last active: {data['last_date']}"
)

    

async def checkin(update: Update, context: ContextTypes.DEFAULT_TYPE):
        if today_compare != data["last_date"]:
            data["streak"] += 1
            data["last_date"] = today_compare
            with open('./data.json', 'w') as file:
                json.dump(data, file)
            final_message = f"Amazing! Streak updated to {data['streak']} days. See you tomorrow Ali."
            await update.message.reply_text(f"{final_message}")
        else:
            await update.message.reply_text("✅ Already checked in today. Keep coding!")



app = Application.builder().token(TOKEN).build()
app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("streak", streak))
app.add_handler(CommandHandler("checkin", checkin))

app.run_polling()