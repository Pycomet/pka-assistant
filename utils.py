from config import *
from models import *


def get_received_msg(msg):
    "Delete This Message"
    message_id = msg.message_id
    chat = msg.chat
    return chat, message_id


class DbClient:
    "For Reading, Updating & Deleting Spreadsheet Content"

    def __init__(self):
        pass

    def get_all_chats(self) -> list:
        "Fetch All Chat Groups"
        pass

    def get_user(self) -> list:
        "Fetch All Users"
        pass

    def user_exists(self) -> bool:
        "If users exists in list or not"
        pass


db_client = DbClient()
