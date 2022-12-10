from config import *
from models import *


def get_received_msg(msg):
    "Delete This Message"
    message_id = msg.message_id
    chat = msg.chat
    return chat, message_id


class DbClient:
    "For Reading, Updating & Deleting Spreadsheet Content"
    pass
