import requests
import smtplib
from bs4 import BeautifulSoup

TARGET_URL = "https://www.amazon.co.uk/Automate-Boring-Stuff-Python-2nd/dp/1593279922/ref=sr_1_9?crid=G12YA8H6XOZ3" \
             "&keywords=python&qid=1679060293&sprefix=python%2Caps%2C67&sr=8-9"

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/110.0",
    "Accept-Language": "en-GB,en;q=0.5",
}

response = requests.get(TARGET_URL, headers=headers)
response.encoding = "utf-8"
html = response.text

