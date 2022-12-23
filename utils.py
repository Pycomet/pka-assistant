from config import *
from models import *


def get_received_msg(msg):
    "Delete This Message"
    message_id = msg.message_id
    chat = msg.chat
    return chat, message_id


def get_spreadsheet(name: str):
    try:
        service = build("sheets", "v4", credentials=creds)
        spreadsheet = (
            service.spreadsheets()
            .values()
            .get(
                spreadsheetId=SPREADSHEET_ID, range=name
            )
            .execute()
        )

        logging.info("Google Sheet Connected! Fetch Complete")
        data = spreadsheet["values"]
        return data
    except Exception as e:
        logging.error("You do not have permission to access this spreadsheet")
        return []


class DbClient:
    "For Reading, Updating & Deleting Spreadsheet Content"


    def get_users(self) -> list:
        "Fetch All Users IDs in the sheet"
        users = []
        names = get_spreadsheet('Names list')[1::]

        for item in names:
            user = User(
                user_id=item[0], screen_name=item[1], user=item[2], agent=item[3]
            )
            users.append(user)
        return users

    def get_data(self) -> list:

        data = []
        sheets = get_spreadsheet('Sheet4')[1::]

        for item in sheets:
            raw = Data(
                name= item[1],
                club_id= int(item[2]),
                agent= item[7],
                agent_rb= int(item[8]),
                ref_code= item[9],
                group_id= item[10]
            )
            data.append(raw)
        return data


    def get_user(self) -> list:
        "Fetch All Users"
        pass

    def user_exists(self) -> bool:
        "If users exists in list or not"
        pass


db_client = DbClient()
