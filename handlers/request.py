from config import *
from utils import *
from handlers.start import *


def parse_message(message: str) -> tuple:
    match = re.search("(\w+) (\d+) (\w+) (\d+)(?: (\d+))?", message)
    if match:
        try:
            # ref_code could be chip count in chip request
            type, club_id, game_name, player_id, ref_code = match.groups()
            return type, club_id, game_name, player_id, ref_code
        except ValueError:
            type, club_id, game_name, player_id = match.groups()
            return type, club_id, game_name, player_id, None
        except TypeError:
            logging.error("Type Error")
            return None
    return None


@bot.message_handler(content_types=['text'])
def handle_message(message):

    if handler_state.get("Requests", False):
        logging.info("Bot is silent")
    else:
        parsed_message = parse_message(message.text.strip())
        if parsed_message:
            type, club_id, game_name, player_id, ref_code = parsed_message
            response = "Request Type: {} ClubID: {}, GameName: {}, PlayerID: {}, RefCode: {}".format(
                type, club_id, game_name, player_id, ref_code or "None"
            )

            if type.lower() == "club":
                return requestRef(message)

            elif type.lower() == "chip":
                return requestChips(message)

            else:
                return
        else:
            logging.info(
                "Invalid format. Use RequestType ClubID GameName PlayerID RefCode(Optional) \n\nexample: Club 1113888 PPPoker 1209729 1234")
            return


def requestRef(msg):
    "RequestBy Ref"
    response = msg.text.split(" ")

    if len(response) != 4:
        bot.send_message(
            msg.chat.id,
            "Invalid Club Request Response!!"
        )
        return False

    else:

        # validation data
        data = db_client.get_data()
        users = db_client.get_users(name=response[2])

        if len(users) > 0:
            id_list = [i.user_id for i in users]



            for group in data:
                if len(response) == 4:
                    if group.club_id == response[1] and response[3] in id_list:
                        logging.info("Valid Request")

                        # Get User Reference Code if It Exists
                        players = group.agent.strip("\n").split(",")
                        ref_codes = group.ref_code.strip("\n").split(",")

                        if msg.from_user.username in players:
                            position = players.index(str(msg.from_user.username))

                            bot.send_message(
                                int(group.group_id),
                                f"Join Club Request From @{msg.from_user.username}: \n\nClub: {group.name} \n\nPlayer ID: {response[3]} \n\nPlayer Ref Code: {ref_codes[position]}",
                                parse_mode="html"
                            )
                        else:
                            bot.send_message(
                                int(group.group_id),
                                f"Join Club Request From @{msg.from_user.username}: \n\nClub: {group.name} \n\nPlayer ID: {response[3]} ",
                                parse_mode="html"
                            )

                        bot.send_message(
                            msg.chat.id,
                            f"Ticket Created 🎫"
                        )

                        return True
                else:
                    
                    if group.club_id == response[1] and response[4] in ref_codes and response[3] in id_list:
                        logging.info("Valid Request")

                        bot.send_message(
                            int(group.group_id),
                            f"Join Club Request From @{msg.from_user.username}: \n\nClub: {group.name} \n\nPlayer ID: {response[3]} \n\nReference Code: {group.ref_code}",
                            parse_mode="html"
                        )

                        bot.send_message(
                            msg.chat.id,
                            f"Ticket Created 🎫"
                        )

                        return True

        bot.send_message(
            msg.chat.id,
            f"Hi customer, there are 2 reasons why this is happening, \n\nYour ID is not registered in our database. @{ADMIN} please adjust, kindly wait for our customer support to add and acknowledge that before you may continue to request once more \
                \n\nYou're a noob and typo, please try once more \n\nThank you",
            parse_mode="html"
        )
        return True


def requestChips(msg):
    "RequestBy Ref"
    response = msg.text.split(" ")

    if len(response) != 5:
        bot.send_message(
            msg.chat.id,
            "Invalid Chip Request Response!!"
        )
        return False

    else:

        # validation data
        data = db_client.get_data()
        users = db_client.get_users(name=response[2])

        if len(users) > 0:
            id_list = [i.user_id for i in users]

            for each in data:
                if each.club_id == response[1] and response[3] in id_list:
                    logging.info("Valid Request")

                    bot.send_message(
                        int(each.group_id),
                        f"Club Chips Request From @{msg.from_user.username}: \n\nClub: {each.name} \n\nPlayer ID: {response[3]} \n\nChips Needed: {response[4]}",
                        parse_mode="html"
                    )

                    bot.send_message(
                        msg.chat.id,
                        f"Ticket Created 🎫"
                    )

                    return True

        bot.send_message(
            msg.chat.id,
            f"Hi customer, there are 2 reasons why this is happening, \n\nYour ID is not registered in our database. @{ADMIN} please adjust, kindly wait for our customer support to add and acknowledge that before you may continue to request once more \
                \n\nYou're a noob and typo, please try once more \n\nThank you",
            parse_mode="html"
        )
        return True
