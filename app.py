from flask import Flask, request
import telegram
from telegram.credentials import bot_token, bot_user_name, URL
from telegram.mastermind import get_response


global bot
global TOKEN
TOKEN = bot_token
bot = telegram.Bot(token=TOKEN)

app= Flask(__name__)

@app.route('/{}'.format(TOKEN), methods=['POST'])
def respond():
    update = telegram.Update.de_json(request.get_json(force=True), bot)
    chat_id = update.message.chat.id
    msg_id = update.message.message_id
    text = update.message.text.encode('utf-8').decode()
    print("got text: ", text)

    response = get_response(text)
    bot.sendMessage(chat_id=chat_id, text=response, reply_to_message_id=msg_id)

@app.route('/setwebhook', methods=['GET', 'POST'])
def set_webhook():
    S =bot.setWebhook('{URL}{HOOK}'.format(URL=URL, HOOK=TOKEN))
    if s:
        return "webhook setup ok"
    else:
        return "webhook setup failed"

@app.route('/')
def index():
    return '.'

if__name__=='main':
    app.run(threaded=True)
