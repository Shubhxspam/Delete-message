import telebot
import os

API_TOKEN = os.getenv('API_TOKEN')

bot = telebot.TeleBot(API_TOKEN)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Welcome! The bot will delete any edited messages immediately.")

@bot.edited_message_handler(func=lambda message: True)
def handle_edited_message(message):
    try:
        bot.delete_message(message.chat.id, message.message_id)
        print(f"Deleted edited message: {message.message_id}")
    except Exception as e:
        print(f"Failed to delete edited message: {e}")

bot.polling()
