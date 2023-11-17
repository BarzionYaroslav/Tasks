import telebot

BOT_TOKEN = input("Write Bot_Token:")
print("Now go to bot or whatever")

bot = telebot.TeleBot(BOT_TOKEN)
@bot.message_handler(func=lambda msg: True)
def echo_all(message):
    bot.reply_to(message, message.text)
bot.infinity_polling()