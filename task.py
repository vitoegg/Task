# -- coding: utf-8 --
import os
import sys
from curl_cffi import requests

COOKIE = os.environ.get("COOKIE", "")

TELEGRAM_BOT_TOKEN = os.environ.get("TELEGRAM_BOT_TOKEN", "")
TELEGRAM_CHAT_ID = os.environ.get("TELEGRAM_CHAT_ID", "")
TELEGRAM_API_URL = "https://api.telegram.org"

def send_telegram_message(token, chat_id, message):
    curl_command = f'curl "{TELEGRAM_API_URL}/bot{token}/sendMessage" -d "chat_id={chat_id}&text={message}"'
    try:
        subprocess.run(curl_command, shell=True, check=True)
        print("Telegram Message Send Successful\n")
    except subprocess.CalledProcessError as e:
        print(f"Telegram Message Send Failed: {e}\n")

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
        print(response_data)
        message = response_data.get('message')
        success = response_data.get('success')
        
        if success == "true":
            print(message)
            if TELEGRAM_BOT_TOKEN and TELEGRAM_CHAT_ID:
                send_telegram_message(TELEGRAM_BOT_TOKEN, TELEGRAM_CHAT_ID, message)
        else:
            print(message)
            if TELEGRAM_BOT_TOKEN and TELEGRAM_CHAT_ID:
                send_telegram_message(TELEGRAM_BOT_TOKEN, TELEGRAM_CHAT_ID, message)

    except Exception as e:
        print("Error:", e)
else:
    print("Set COOKIE First")
