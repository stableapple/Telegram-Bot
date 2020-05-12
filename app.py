from flask import Flask, request
import telegram
import logging
import sys
import os
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext
from telebot.credentials import bot_token, bot_user_name, URL
from telebot.mastermind import get_response
from flask import Flask, current_app, jsonify
from bottle import run, post, request as bottle_request




global bot
global TOKEN
logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger()


TOKEN = bot_token
bot = telegram.Bot(token=TOKEN)



app= Flask(__name__)
with app.app_context():
    # within this block, current_app points to app.
    print(current_app.name)

@app.route('/{}'.format(TOKEN), methods=['POST'])
def respond(update, context: CallbackContext):
    update.message.reply_text("💁 Hi there! Welcome to the COVID19 BOT, Carla. Enter the name of any country, to get updates about the COVID19 situation in that country. Stay Safe!🙇‍♀️")


@app.route('/setwebhook', methods=['GET', 'POST'])
def set_webhook(bot, update):
    s = bot.setWebhook(URL+TOKEN)
    if s:
        return "webhook setup ok"
    else:
        return "webhook setup failed"
@app.route('/{}'.format(TOKEN), methods=['POST'])
def info(update, context: CallbackContext):
    user_input = update.message.text
    response = get_response(user_input)
    update.message.reply_text("🌏"+response +"🌎")

def main():
    app.run(host='localhost', port=7883, debug=True)
    updater = Updater(TOKEN,use_context=True)
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('start', respond))
    dp.add_handler(MessageHandler(Filters.text, info))
    updater.start_polling()
    updater.idle()

if __name__ == "__main__":
    main()
