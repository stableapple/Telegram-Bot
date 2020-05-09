from flask import Flask, request
import telegram
import logging
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from telebot.credentials import bot_token, bot_user_name, URL
from telebot.mastermind import get_response
from flask import Flask, current_app

global bot
global TOKEN
TOKEN = bot_token
bot = telegram.Bot(token=TOKEN)


app= Flask(__name__)
with app.app_context():
    # within this block, current_app points to app.
    print(current_app.name)



@app.route('/{}'.format(TOKEN), methods=['POST'])
def respond(bot, update):
    response = get_response()
    print("Finished")
    bot.send_message(chat_id=update.message.chat_id, text=response)
    print("end")
@app.route('/setwebhook', methods=['GET', 'POST'])
def set_webhook(bot, update):
    s = bot.setWebhook('{URL}{HOOK}'.format(URL=URL, HOOK=TOKEN))
    if s:
        return "webhook setup ok"
    else:
        return "webhook setup failed"
@app.route('/{}'.format(TOKEN), methods=['POST'])
def echo(bot, update):
    print("echo")
    """Echo the user message."""
    bot.send_message(chat_id=update.message.chat_id, text=update.message.text)


def main():
    app.run(threaded=True)
    updater = Updater(TOKEN)
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('start', respond))
    dp.add_handler(MessageHandler(Filters.text,echo ))
    updater.start_polling()
    updater.idle()

if __name__ == "__main__":
    main()
