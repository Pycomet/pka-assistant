from models import User
import asyncio
import logging
import os
import re
from flask import Flask, request
import telebot
from telebot import types
from datetime import date
from dotenv import load_dotenv
load_dotenv()


user = User
LANGUAGE = user.language

# # Language setup
# os.environ["LANGUAGE"] = "en"
# LANGUAGE = os.getenv("LANGUAGE")
# Logging Setup
logging.basicConfig(
    format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
    level=logging.INFO
)

TOKEN = os.getenv('TOKEN')
API_ID = os.getnv('API_ID')
API_HASH = os.getenv('API_HASH')

DEBUG = True
SERVER_URL = os.getenv("SERVER_URL")

bot = telebot.TeleBot(token=TOKEN)
app = Flask(__name__)
