from config import *
from utils import *

# def start_menu(msg):
#     keyboard = types.ReplyKeyboardMarkup(row_width=2)

#     a = types.KeyboardButton(
#         translator.translate("I Am A Passenger?", LANGUAGE))
#     b = types.KeyboardButton(translator.translate(
#         "I Am A Bus Operator?", LANGUAGE))
#     c = types.KeyboardButton(translator.translate("Referral Link", LANGUAGE))
#     d = types.KeyboardButton(translator.translate("About Us", LANGUAGE))
#     e = types.KeyboardButton(translator.translate(
#         "Rules & Regulations", LANGUAGE))
#     f = types.KeyboardButton("Language Switcher")
#     g = types.KeyboardButton("Contact Us")

#     keyboard.add(a, b, c, d, e, f, g)
#     return keyboard


@bot.message_handler(commands=['start'])
def startbot(msg):
    "Entry point of the bot discussion -- https://ibb.co/1Mvm7GN"

    bot.send_chat_action(msg.from_user.id, "typing")

    if hasattr(msg, "message_id"):
        chat, m_id = get_received_msg(msg)
        bot.delete_message(chat.id, m_id)

    user.id = msg.from_user.id

    bot.send_photo(
        msg.from_user.id,
        photo=" https://ibb.co/1Mvm7GN",
        caption=f"🤡 Welcome {msg.from_user.first_name}, \n\nI am the Offical <b>PKA Assistant</b> Bot \n\nFor more information join our main channel. Contact @... to get access rights",
        parse_mode="html",
    )


@ bot.message_handler(regexp="^Back")
def startbotn(msg):
    startbot(msg)
