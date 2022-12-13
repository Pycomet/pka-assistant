from google.api_core.exceptions import PermissionDenied
from google.auth.transport.requests import Request
from google.oauth2.service_account import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
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
creds = Credentials.from_service_account_file('./keys.json')


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
    service = build('sheets', 'v4', credentials=creds)
    spreadsheet = service.spreadsheets().values().get(
        spreadsheetId='1F33sEAoZBdXzsggFW317sBff2P0pAwZmAsPkPV5Io6Y', range='A1:G9').execute()

    logging.info("Google Sheet Connected!")
    data = spreadsheet['values']
    logging.info(data)
except PermissionDenied:
    logging.error("You do not have permission to access this spreadsheet")
