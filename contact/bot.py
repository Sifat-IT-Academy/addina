import requests
from environs import Env

env = Env()
env.read_env()

def send_message(text):
    BOT_TOKEN = env("BOT_TOKEN")
    CHAT_ID = env("CHAT_ID")
    TEXT = text
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage?chat_id={CHAT_ID}&text={TEXT}"
    
    try:
        response = requests.get(url)
        response.raise_for_status()
        print(f"Message sent successfully, status code: {response.status_code}")
    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP error occurred: {http_err}")
    except Exception as err:
        print(f"Other error occurred: {err}")


