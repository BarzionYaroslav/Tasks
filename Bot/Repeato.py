import telebot

BOT_TOKEN = "6419650660:AAHs1XL7LS3eebu98lYEM9Lq_o36W4SD268"

bot = telebot.TeleBot(BOT_TOKEN)
@bot.message_handler(func=lambda msg: True)
def echo_all(message):
    bot.reply_to(message, message.text)
bot.infinity_polling()