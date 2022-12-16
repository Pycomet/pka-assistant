from config import *
from utils import *

def start_menu():
    keyboard = types.InlineKeyboardMarkup(row_width=2)

    a = types.InlineKeyboardButton("Club Request", callback_data="request")
    b = types.InlineKeyboardButton("Chip Request", callback_data="chip")
    c = types.InlineKeyboardButton("Rake Back", callback_data="rake_back")
    d = types.InlineKeyboardButton("View All Clubs", callback_data="all_clubs")
    e = types.InlineKeyboardButton("Transactions", callback_data="payment")
    # e = types.InlineKeyboardButton("🔙 Go Back" callback_data="back")

    keyboard.add(a, b, c, d, e)
    return keyboard


@bot.message_handler(commands=["start"])
def startbot(msg):
    "Entry point of the bot discussion -- https://ibb.co/1Mvm7GN"

    bot.send_chat_action(msg.from_user.id, "typing")

    if hasattr(msg, "message_id") and msg.chat.type != 'group':
        chat, m_id = get_received_msg(msg)
        bot.delete_message(chat.id, m_id)


    if msg.chat.type != 'group':
        bot.send_photo(
            msg.chat.id,
            photo="https://ibb.co/1Mvm7GN",
            caption=f"{msg.from_user.first_name} Welcome, \n\nI am the Offical PKA Assistant Bot \n\nFor more information join our main channel. Contact @... to get access rights",
            parse_mode="html",
            reply_markup=start_menu(),
        )
    else:
        bot.send_photo(
            msg.chat.id,
            photo="https://ibb.co/1Mvm7GN",
            caption=f"I am the Offical PKA Assistant Bot For All Clubs \n\nFor more information join our main channel. Contact me @pkaassistantbot",
            parse_mode="html"
        )



@bot.callback_query_handler(func=lambda c: True)
def button_callback_answer(call):
    """
    Button Response
    """
    bot.send_chat_action(call.from_user.id, "typing")

    if call.data == "request":
        question = bot.send_message(
            call.from_user.id,
            f"Write request in this format: ClubID PlayerID RefCode \n\nexample: 34545345 3453453 234523",
            parse_mode="html"
        )

        bot.register_next_step_handler(question, requestRef)

    elif call.data == "chip":

        question = bot.send_message(
            call.from_user.id,
            f"Write request in this format: ClubID PlayerID Chips needed to depoit or withdraw \n\nexample: 34545345 3453453 500",
            parse_mode="html"
        )

        bot.register_next_step_handler(question, requestChips)

    elif call.data == "rake_back":
        question = bot.send_message(
            call.from_user.id,
            f"Write request the full club name",
            parse_mode="html"
        )

        bot.register_next_step_handler(question, rakebot)
    
    elif call.data == "all_clubs":
        "Returns A List Of All Clubs"
        data = db_client.get_data()

        keyboard = types.InlineKeyboardMarkup(row_width=1)
        [keyboard.add(types.InlineKeyboardButton(f"{item.name} (ID- {item.club_id})", callback_data="test")) for item in data]

        bot.send_message(
            chat_id=call.from_user.id,
            text="🏁 Here are the list of all our groups;",
            reply_markup=keyboard
        )


    elif call.data == "payment":

        bot.send_message(
            call.from_user.id,
            f"Here are the payment options; \
                \n\nUsdt \n0x0638ca8548c88c5a3c260fb5f8dbb9aaf5ff67da \
                \n\nBtc \n1Gdm42Y62fPqUPdULYr36weii8tdqeGYST \
                \n\nTrc20 \nTPQF3fmPV1EE6acTivwEjC1VywuVKAd8JA \
                \n\nFor more options or help, contact @{ADMIN}"
        )

    else:
        pass



def rakebot(msg):
    "Get response for club name"

    bot.send_chat_action(msg.from_user.id, "typing")
    name = msg.text.lower()

    data = db_client.get_data()

    for group in data:
        if group.name.lower() == name:
            # VALID RESPONSE
            bot.send_message(
                msg.from_user.id,
                f"Rake Back Response: \n\nAgent/Player: {group.agent} \nRB Score: {group.agent_rb}",
                parse_mode="html"
            )

            return True

    bot.send_message(
        msg.from_user.id,
        "Invalid Club Name!!"
    )
    return False





def requestRef(msg):
    "RequestBy Ref"
    response = msg.text.split(" ")

    if len(response) != 3:
        bot.send_message(
            msg.from_user.id,
            "Invalid Response!!"
        )
        return False

    else:
        
        # validation data
        data = db_client.get_data()
        users = db_client.get_users()

        id_list = [i.user_id for i in users]

        for each in data:
            if each.club_id == int(response[0]) and each.ref_code == response[2] and response[1] in id_list:
                logging.info("Valid Request")

                bot.send_message(
                    int(each.group_id),
                    f"Join Club Request From {msg.from_user.id}: \n\nClub: {each.name} \n\nPlayer ID: {response[1]} \n\nReference Code: {each.ref_code}",
                    parse_mode="html"
                )
            
                bot.send_message(
                    msg.from_user.id,
                    f"Ticket Created 🎫"
                )

                return True

        bot.send_message(
            msg.from_user.id,
            f"Invalid IDs Submitted Contact Support @{ADMIN}!!"
        )
        return True






def requestChips(msg):
    "RequestBy Ref"
    response = msg.text.split(" ")

    if response.length != 3:
        bot.send_message(
            msg.from_user.id,
            "Invalid Response!!"
        )
        return False

    else:
        
        # validation data
        data = db_client.get_data()
        users = db_client.get_users()

        id_list = [i.user_id for i in users]

        for each in data:
            if each.club_id == int(response[0]) and response[1] in id_list:
                logging.info("Valid Request")

                bot.send_message(
                    int(each.group_id),
                    f"Club Chips Request From {msg.from_user.id}: \n\nClub: {each.name} \n\nPlayer ID: {response[1]} \n\nChips Needed: {response[2]}",
                    parse_mode="html"
                )

                bot.send_message(
                    msg.from_user.id,
                    f"Ticket Created 🎫"
                )

                return True
                
        bot.send_message(
            msg.from_user.id,
            f"Invalid IDs Submitted Contact Support @{ADMIN}!!"
        )
        return True
