import logging
from telegram import Update

from telegram.ext import (
    Updater,
    CommandHandler,
    MessageHandler,
    CallbackQueryHandler,
    Filters
    )

from help import help, button

from modules import (
    welcome,
    config,
    send,
    reply,
    write_admins,
    read_admins,
    read_users,
    chat
    )

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)

def error(update, context):
    logger.warning('Update "%s" caused error "%s"', update, context.error)

if __name__ == '__main__':
    
    TOKEN = config['bot_token']
    
    updater = Updater(TOKEN, use_context=True)
    dp_add = updater.dispatcher.add_handler

    dp_add(CommandHandler("start", welcome))
    dp_add(CommandHandler("help", help))
    dp_add(CallbackQueryHandler(button))
    dp_add(CommandHandler('send', send))
    dp_add(CommandHandler('reply', reply))
    dp_add(CommandHandler('write_admins', write_admins))
    dp_add(CommandHandler('read_admins', read_admins))
    dp_add(CommandHandler('read_users', read_users))

    dp_add(MessageHandler(Filters.text, chat))
    
    updater.dispatcher.add_error_handler(error)

    updater.start_polling()
