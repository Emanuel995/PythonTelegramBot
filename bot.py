from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from telegram import ChatAction

def start(update,context):
    update.message.reply_text('Hola, '+str(update.message.chat.username)+'!.... Estoy vivo!!')

def bye(update,context):
    update.message.reply_text('a la camita... a mimirr...')
    chat = update.message.chat
    chat.send_photo(
        photo = open("amimir.jpg",'rb')
    )
    

if __name__ == '__main__':
    updater = Updater(token='1696726088:AAEqIJbF61Y9p9LWxE7tvaGca_pJ5P_8t-w', use_context=True)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler('start',start))
    dp.add_handler(CommandHandler('bye',bye))

    updater.start_polling()
    updater.idle()