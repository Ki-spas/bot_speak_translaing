import telebot
"""from config import TOKEN"""
from logic import get_fact
from logic import speak


bot = telebot.TeleBot("")

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, f"Привет! {message.from_user.first_name }Я твой Telegram бот  для озвучки факта ")

@bot.message_handler(commands=['fact'])
def bot_weather(message):
    parts = message.text.split(maxsplit=1)
    if len(parts) < 2 :
        bot.reply_to (message , "")
        return
    else:
        fact_for = get_fact()
        bot.reply_to(message , fact_for)
        speak(fact_for)

if __name__ == "__main__":
    bot.infinity_polling()

