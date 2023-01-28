# from google.api_core.exceptions import PermissionDenied
# from google.auth.transport.requests import Request
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
creds = Credentials.from_service_account_file("./keys.json")


# Logging Setup
logging.basicConfig(
    format="[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s", level=logging.INFO
)

TOKEN = os.getenv("TOKEN")

DEBUG = True
SERVER_URL = os.getenv("SERVER_URL")
ADMIN = os.getenv('ADMIN')

bot = telebot.TeleBot(token=TOKEN)
app = Flask(__name__)

SPREADSHEET_ID = os.getenv("SPREADSHEET_ID")
