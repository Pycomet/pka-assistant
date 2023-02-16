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

    bot.send_message(
        msg.chat.id,
        f"{msg.from_user.first_name} Welcome, \n\nI am the Offical PKA Assistant Bot \n\nFor more information join our main channel. Contact @... to get access rights",
        parse_mode="html",
        reply_markup=start_menu(),
    )


@bot.callback_query_handler(func=lambda c: True)
def button_callback_answer(call):
    """
    Button Response
    """
    bot.send_chat_action(call.message.chat.id, "typing")

    if call.data == "request":
        bot.send_message(
            call.message.chat.id,
            f"Write request in this format: RequestType ClubID GameName PlayerID RefCode(Optional) \n\nexample: Club 1113888 PPPoker 1209729 1234",
            parse_mode="html"
        )

        # bot.register_next_step_handler(question, requestRef)

    elif call.data == "chip":

        bot.send_message(
            call.message.chat.id,
            f"Write request in this format: RequestType ClubID GameName PlayerID Chips needed to depoit or withdraw \n\nexample: Chip 1113888 PPPoker 1209729 500",
            parse_mode="html"
        )

        # bot.register_next_step_handler(question, requestChips)

    elif call.data == "rake_back":
        question = bot.send_message(
            call.message.chat.id,
            f"Write request the full club name",
            parse_mode="html"
        )

        bot.register_next_step_handler(question, rakebot)

    elif call.data == "all_clubs":
        "Returns A List Of All Clubs"
        bot.send_chat_action(call.message.chat.id, "typing")
        data = db_client.get_data()

        keyboard = types.InlineKeyboardMarkup(row_width=1)
        [keyboard.add(types.InlineKeyboardButton(
            f"{item.name} (ID- {item.club_id})", callback_data="test")) for item in data]

        bot.send_message(
            chat_id=call.message.chat.id,
            text="🏁 Here are the list of all our active(only) clubs ;",
            reply_markup=keyboard
        )

    elif call.data == "payment":

        bot.send_message(
            call.message.chat.id,
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
            players = group.agent.strip("\n").split(",")
            players_rb = group.agent_rb.strip("\n").split(",")
            players_ref = group.ref_code.strip("\n").split(",")

            if str(msg.from_user.username) in players:
                position = players.index(str(msg.from_user.username))
                # VALID RESPONSE
                bot.send_message(
                    msg.chat.id,
                    f"Rake Back Response For <b>{group.name}</b>: \n\n<b>Agent/Player</b>: {players[position]} \n<b>RB Score(s)</b>: {players_rb[position]} \n<b>Ref Code</b>: {players_ref[position]}",
                    parse_mode="html"
                )
            else:
                bot.send_message(
                    msg.chat.id,
                    f"Rake Back Response For <b>{group.name}</b>: \n\n<b>Agent/Player</b>: {msg.from_user.username} \n<b>RB Score(s)</b>: No Rake Back ",
                    parse_mode="html"
                )

            return True

    bot.send_message(
        msg.chat.id,
        "Invalid Club Name!!"
    )
    return False
