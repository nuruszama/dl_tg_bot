import json

from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup

from telegram.ext import CallbackContext, CallbackQueryHandler

with open('config.json') as f:
    config = json.load(f)

def guide(update, context: CallbackContext):
    click = InlineKeyboardButton
    keyboard = [
                [
                click("Send", callback_data='1'),
                click("Edit", callback_data='2'),
                click("Delete", callback_data='3'),
                ],
                [
                click("msg_id", callback_data='4'),
                click("About_you", callback_data='5'),
                ],
                [
                click("Pin", callback_data='6'),
                click("Unpin", callback_data='7'),
                click("Math", callback_data='8'),
                ]
               ]

    reply_markup = InlineKeyboardMarkup(keyboard)
    update.message.reply_text(
        "Help 🤔!\nFollowing are the tasks I can handle\n"
        "choose any one to know how to use it",
                              reply_markup=reply_markup)

def miss_guide(update, context):
    update.message.reply_text("Sorry. No help files found")

def help (update, context):
    chatid = update.message.chat_id
    idd = str(chatid)
    user = update.message.from_user
    if idd not in config["owner_chat_id"]:
        miss_guide(update, context)
    if idd in config["owner_chat_id"]:
        guide(update, context)

def button(update, context=CallbackQueryHandler):
    query = update.callback_query
    if query.data == '1':
        message = ("Forward a message to a group or channel\n"
              "Usage: use /send and send me the message and chat id when I ask you")
    elif query.data == '2':
        message = ("Edits a message send by me\n"
              "Usage: reply to message which you want to edit with /edit_msg"
              "\nI should be an admin to edit other members messages")
    elif query.data == '3':
        message = ("Deletes a message send by anyone\n"
              "Usage: reply to message which you want to delete with /delete"
              "\nI should be an admin to delete other members message")
    elif query.data == '4':
        message = ("Show you the message id of your message\n"
              "Usage: send me /msg_id and I will tell you tour last message id")
    elif query.data == '5':
        message = ("Gives you basic info about you\n"
              "Usage: send me /about_me and I will tell you about you")
    elif query.data == '6':
        message = ("Pin message for you in personal and public chat\n"
              "Usage: reply to a message with /pin to pin that message")
    elif query.data == '7':
        message = ("Unpin a pinned message for you in personal and public chat\n"
              "Usage: reply to a message with /unpin to pin that message")
    elif query.data == '8':
        message = ("mute someone in group chats\n"
              "Usage: send plain number maths, I will evaluate it\n"
              "I can do--> \n[+] addition\n[-] substration\n[*] Multiplication\n"
              "[/] divition\n[**] exponetiation\n\nEg: send like '3+8*7'")
    context.bot.editMessageText(text = message,
                                chat_id=query.message.chat_id,
                                message_id=query.message.message_id)



