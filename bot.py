from telegram.ext import Updater, CommandHandler

def start(update,context):
    update.message.reply_text('Hola Flor!.... Estoy vivo!!')

if __name__ == '__main__':
    updater = Updater(token='1696726088:AAEqIJbF61Y9p9LWxE7tvaGca_pJ5P_8t-w', use_context=True)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler('start',start))

    updater.start_polling()
    updater.idle()