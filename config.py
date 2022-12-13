from google.api_core.exceptions import PermissionDenied
from google.oauth2.credentials import Credentials
from googleapicliuent.discovery import build
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

# Google sheet libraries
credentials = Credentials.from_service_account_file('./keys.json')
# Create a service object for interacting with the API
service = build('sheets', 'v4', credentials=credentials)

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

DEBUG = True
SERVER_URL = os.getenv("SERVER_URL")

bot = telebot.TeleBot(token=TOKEN)
app = Flask(__name__)


# Use the service object to access the API and get the spreadsheet
try:
    spreadsheet = service.spreadsheets().get(
        spreadsheetId='<spreadsheet_id>').execute()
except PermissionDenied:
    print("You do not have permission to access this spreadsheet")
