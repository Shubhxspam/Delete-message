def delete_edited_message(bot, message):
    chat_id = message.chat.id
    message_id = message.message_id
    bot.delete_message(chat_id, message_id)
