import telebot

# Replace 'YOUR_BOT_TOKEN' with your actual bot token
bot = telebot.TeleBot('YOUR_BOT_TOKEN')

@bot.message_handler(func=lambda message: True)
def handle_message(message):
    if message.from_user.username == 'UR TARGET USERNAME':
        bot.reply_to(message, "THE MASSAGE THAT U WANT TO SEND")

bot.polling()