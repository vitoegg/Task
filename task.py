import os
import sys
import subprocess
import json
from curl_cffi import requests

COOKIE = os.environ.get("COOKIE", "")

TELEGRAM_BOT_TOKEN = os.environ.get("TELEGRAM_BOT_TOKEN", "")
CHAT_ID = os.environ.get("CHAT_ID", "")
TELEGRAM_API_URL = os.environ.get("TELEGRAM_API_URL", "https://api.telegram.org")

def send_telegram_notification(message):
    url = f'{TELEGRAM_API_URL}/bot{TELEGRAM_BOT_TOKEN}/sendMessage'
    data = json.dumps({
        'chat_id': CHAT_ID,
        'text': message
    })
    curl_command = [
        'curl', '-X', 'POST',
        '-H', 'Content-Type: application/json',
        '-d', data,
        url
    ]
    try:
        result = subprocess.run(curl_command, capture_output=True, text=True)
        print("Telegram notification sent.")
    except Exception as e:
        print("Error sending Telegram notification")

if COOKIE:
    url = f"https://www.nodeseek.com/api/attendance?random=true"
    headers = {
        'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36 Edg/125.0.0.0",
        'sec-ch-ua': "\"Not A(Brand\";v=\"99\", \"Microsoft Edge\";v=\"121\", \"Chromium\";v=\"121\"",
        'sec-ch-ua-mobile': "?0",
        'sec-ch-ua-platform': "\"Windows\"",
        'origin': "https://www.nodeseek.com",
        'sec-fetch-site': "same-origin",
        'sec-fetch-mode': "cors",
        'sec-fetch-dest': "empty",
        'referer': "https://www.nodeseek.com/board",
        'accept-language': "zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6",
        'Cookie': COOKIE
    }

    try:
        response = requests.post(url, headers=headers)
        response_data = response.json()
        
        message = response_data.get('message')
        result = response_data.get('success')
        
        send_telegram_notification(message)
        print("Signin Status:" result)
        
    except json.JSONDecodeError:
        print("Error decoding API response.")
    except Exception as e:
        print("An error occurred during the operation.")
else:
    print("Cookie not set. Please configure the environment variable.")
