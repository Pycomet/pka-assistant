from config import *
from utils import *


def start_menu():
    keyboard = types.ReplyKeyboardMarkup(row_width=2)

    a = types.KeyboardButton("Offical Channel")
    b = types.KeyboardButton("Poker Group")
    c = types.KeyboardButton("Rake Group")

    keyboard.add(a, b, c)
    return keyboard


@bot.message_handler(commands=['start'])
def startbot(msg):
    "Entry point of the bot discussion -- https://ibb.co/1Mvm7GN"

    bot.send_chat_action(msg.from_user.id, "typing")

    if hasattr(msg, "message_id"):
        chat, m_id = get_received_msg(msg)
        bot.delete_message(chat.id, m_id)

    bot.send_photo(
        msg.from_user.id,
        photo="https://ibb.co/1Mvm7GN",
        caption=f"🤡 Welcome {msg.from_user.first_name}, \n\nI am the Offical PKA Assistant Bot \n\nFor more information join our main channel. Contact @... to get access rights",
        parse_mode="html",
        reply_markup=start_menu()
    )


@ bot.message_handler(regexp="^Back")
def startbotn(msg):
    startbot(msg)
