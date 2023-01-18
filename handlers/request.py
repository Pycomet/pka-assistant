from config import *
from utils import *
from handlers.start import *

@bot.message_handler(func=lambda message: True)
def requestbot(msg):
    "Request Bot Handler For Groups"

    if msg.chat.type == 'group':

        requestRef(msg)
    
    else:
        print(msg)
