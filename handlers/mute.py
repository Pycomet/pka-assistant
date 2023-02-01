from config import *
from utils import *


@bot.message_handler(commands=["mute"])
def mutebot(msg):
    "Mute The Bot From Responding"
    global SILENT

    if hasattr(msg, "message_id") and msg.chat.type != 'group':
        chat, m_id = get_received_msg(msg)
        bot.delete_message(chat.id, m_id)

    if msg.from_user.username == ADMIN:
        handler_state["Requests"] = True
        bot.send_message(
            msg.chat.id,
            f" 🔇 Silent Mode Activated. \n\nThis Bot Would Not Take Any Incoming Requests",
            parse_mode="html",
        )


@bot.message_handler(commands=["unmute"])
def mutebot(msg):
    "Mute The Bot From Responding"

    if hasattr(msg, "message_id") and msg.chat.type != 'group':
        chat, m_id = get_received_msg(msg)
        bot.delete_message(chat.id, m_id)

    if msg.from_user.username == ADMIN:
        handler_state["Requests"] = False
        bot.send_message(
            msg.chat.id,
            f" 🔊 Silent Mode Deactivated. \n\nBot is Actively Taking Requests",
            parse_mode="html",
        )
