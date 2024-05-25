import telebot
import os

API_TOKEN = os.getenv('API_TOKEN')

bot = telebot.TeleBot(API_TOKEN)

@bot.message_handler(commands=['estart'])
def send_welcome(message):
    bot.reply_to(message, "Welcome! The bot will delete any edited messages immediately ,support group - @Mrpasserby_1227.")

@bot.edited_message_handler(func=lambda message: True)
def handle_edited_message(message):
    try:
        bot.delete_message(message.chat.id, message.message_id)
        print(f"Deleted edited message: {message.message_id}")
    except Exception as e:
        print(f"Failed to delete edited message: {e}")

bot.polling()

@bot.command()
async def ebroadcast(ctx, *, message):
    for guild in bot.guilds:
        for channel in guild.text_channels:
            try:
                await channel.send(message)
            except Exception as e:
                print(f"Failed to send message to {channel}: {e}")

@bot.command()
async def estats(ctx):
    guild_count = len(bot.guilds)
    await ctx.send(f"The bot is in {guild_count} servers.")
