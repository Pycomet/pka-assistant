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
        print(data)
        return data
    except Exception as e:
        logging.error("You do not have permission to access this spreadsheet")
        return []


class DbClient:
    "For Reading, Updating & Deleting Spreadsheet Content"

    def get_users(self, name: str = "") -> list:
        "Fetch All Users IDs in the sheet By Club Name"
        # BY CLUB NAME NOT IMPLEMENTED YET!!
        users = []
        names = get_spreadsheet(name)[1::]

        for item in names:
            try:
                user = User(
                    user_id=int(item[0]) or 0,
                    screen_name=item[1] or "",
                    user=item[2] or "",
                    agent=item[3] or ""
                )
                users.append(user)
            except:
                logging.warn(f"Issue writing User to Model - {item}")
        return users

    def get_data(self) -> list:

        data = []
        sheets = get_spreadsheet('Sheet33!A1:Q44')[1::]

        for item in sheets:
            if item[4] == "Yes":
                raw = Data(
                    name=item[0],
                    club_id=item[2],
                    agent=item[14],
                    agent_rb=item[13],
                    ref_code=item[16] if len(item) > 16 else "",
                    group_id=item[15]
                )
                data.append(raw)
            else:
                logging.warn(f"Inactive Chat Group - {item[0]}")

        print(data)
        return data

    def get_user(self) -> list:
        "Fetch All Users"
        pass

    def user_exists(self) -> bool:
        "If users exists in list or not"
        pass


db_client = DbClient()
