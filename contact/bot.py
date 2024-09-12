import requests

from environs import Env

env = Env()
env.read_env()


def  send_message(text):
  BOT_TOKEN = env.str("BOT_TOKEN")
  CHAT_ID = env.str("CHAT_ID")
  PHOTO = "https://i.pinimg.com/originals/85/c8/3d/85c83d242b73d3c52b8c4c2e7df27db7.jpg"
  TEXT = text
  url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendphoto?chat_id={CHAT_ID}&photo={PHOTO}&caption={TEXT}"
  response = requests.get(url)
