# dl_tg_bot
Assuming you have environment set to run python programs, this is a telegram bot with a simple deep learning.

To run this bot you need some libraries installed.

1. telegram_bot_api
2. numpy
3. keras
4. nltk

Next you need telegram api generated from BOT FATHER.
Now we need a config.json. We will mention bot api, some valid users who can access our bot and our own chat id in it.
config.json should be like this.
{
   "valid_users": [
       "user_1's chat_id",
       "user_2's chat_id"
   ],
   "bot_token": "replace with token from BOT FATHER",
   "owner_chat_id": "your chat_id"
}

All set to run the training. I have some message data written in intents.json. Now you have to run training.py which will learn intents.json and  create words.pkl, classes.pkl and chatbot_model.h5 which we need to run chat with bot. As we give more data to intents.json, accuracy of bot increases.

Final step to activate our bot is to just run main.py
wola.. now have a chat with your bot in telegram. 1st message reply will take some time depending on specs of your machine. Later it will work fine.
