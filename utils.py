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

    def get_all_users(self) -> list:
        "Fetch All Users IDs in the sheet"
        users = []

        for item in users_data[1::]:
            user = User(
                user_id=item[0],
                screen_name=item[1],
                user=item[2],
                agent=item[3]
            )
            users.append(user)
        print(users)
        return users

    def get_user_ids(self) -> list:
        "Fetch All Users IDs in the sheet"
        user_ids = [item[0] for item in users_data]
        return user_ids[1::]

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
