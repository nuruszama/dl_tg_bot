import logging
import json
import random
from telegram import Update
from telegram.ext import CallbackContext
from chat_bot import chatbot_response

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

with open('config.json') as f:
    config = json.load(f)


def add_user(update, context):
    chatid = str(update.message.chat_id)
    user = update.message.from_user
    username = "{}".format(user['username'])
    users = {chatid : (f"@{username}")}
    with open ("users.json", "r") as file:
        old_data = str(json.load(file))
        old = old_data.replace("}", ",")
        new = str(users)
        new = new.replace("{", " ")
        new_data = old+new
        new_data = new_data.replace("'", '"')

    with open("users.json", "w") as f:
        f.write(str(new_data))

def read_users(update, context):
    with open("users.json", "r") as openfile:
        users = json.load(openfile)
        update.message.reply_text(users)

def welcome(update, context):
    chatid = update.message.chat_id
    idd = str(chatid)
    user = update.message.from_user
    context.bot.send_message(chat_id=config["owner_chat_id"], text=
        "Chat initiated by user {} {}  [@{}]"
                .format(user['first_name'],user['last_name'],user['username']))
    logging.info("[System Log] Chat initiated by user {}".format(user['username']))
    context.bot.send_message(chat_id=chatid, text=
        "Hi {} 🙂 I'm Aleesa, a telegram bot 🤖\n"
        "Use /help to know more".format(user['first_name']))


def send(update: Update, context: CallbackContext):
    chatid = update.message.chat_id
    idd = str(chatid)
    user = update.message.from_user
    if idd not in config["owner_chat_id"]:
        context.bot.send_message(
            text= "You are not authorised to use this command", chat_id=chatid
            )
    if idd in config["owner_chat_id"]:
        text = context.args
        msgs = ' '.join([str(item) for item in text])
        msg = msgs.split('+')
        context.bot.send_message(text=msg[0], chat_id=msg[1])
        update.message.reply_text("Done")


def reply(update: Update, context: CallbackContext):
    chatid = update.message.chat_id
    idd = str(chatid)
    user = update.message.from_user
    if idd not in config["owner_chat_id"]:
        context.bot.send_message(
            text= "You are not authorised to use this command", chat_id=chatid
            )
    if idd in config["owner_chat_id"]:
        text = context.args
        msgs = ' '.join([str(item) for item in text])
        msg = msgs.split('+')
        context.bot.send_message(text=msg[0], chat_id=msg[1], reply_to_message_id=msg[2])
        update.message.reply_text("Done") 


def chat(update, context):
    msg = update.message.text
    chatbot_response(msg)
    if msg != '':
        res = chatbot_response(msg)
    update.message.reply_text(res)


def write_admins(update, context):
    chatid = update.message.chat_id
    idd = str(chatid)
    user = update.message.from_user
    if idd not in config["owner_chat_id"]:
        update.message.reply_text(
            "You are not authorised to use this command"
            )
    if idd in config["owner_chat_id"]:
        admins ={
            "fullname" : "Abdul Samad",
            "username" : "nuruszama",
            "user_id" : "688872009"
            }
        with open ("admins.json", "w") as outfile:
            json.dump(admins, outfile)


def read_admins(update, context):
    chatid = update.message.chat_id
    idd = str(chatid)
    user = update.message.from_user
    if idd not in config["owner_chat_id"]:
        update.message.reply_text(
            "You are not authorised to use this command"
            )
    if idd in config["owner_chat_id"]:
        with open("admins.json", "r") as openfile:
            admins = json.load(openfile)
            update.message.reply_text(admins)
            
