from time import time
import requests
import json
import time
from telegram.ext import *

token = "Geheim"

url = f"https://api.telegram.org/bot{token}/sendMessage"
#message = requests.post(url, params=params)

def sample_responses(input_text):
    user_message = str(input_text).lower()
    if user_message == "status":
        return "aktiv"
    if user_message == "screenshot":
        return "screenshot"

def notification(msg):
    params = {"chat_id":"761757707", "text":msg}
    url = f"https://api.telegram.org/bot{token}/sendMessage"
    requests.post(url, params=params)

