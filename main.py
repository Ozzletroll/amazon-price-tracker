import os
import requests
import smtplib
from bs4 import BeautifulSoup

TARGET_URL = "https://www.amazon.co.uk/Automate-Boring-Stuff-Python-2nd/dp/1593279922/ref=sr_1_9?crid=G12YA8H6XOZ3" \
             "&keywords=python&qid=1679060293&sprefix=python%2Caps%2C67&sr=8-9"
PRICE_THRESHOLD = 25.00

email_1 = os.environ["FROM_EMAIL"]
app_password = os.environ["APP_PASSWORD"]
email_2 = os.environ["TO_EMAIL"]

# HTML request
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/110.0",
    "Accept-Language": "en-GB,en;q=0.5",
}
response = requests.get(TARGET_URL, headers=headers)
response.encoding = "utf-8"
html = response.text

# Scrape html data with BeautifulSoup and get current item price
soup = BeautifulSoup(html, "html.parser")
current_price = soup.find(name="span", class_="a-size-base a-color-price a-color-price").getText()
current_price = float(current_price.replace("£", ""))

# Check if current item price is below threshold and send email alert
item_name = soup.find(name="span", id="productTitle").getText()
message = f"{item_name} is currently {current_price}.\n\n {TARGET_URL}."
message.encode("utf-8")

if current_price < PRICE_THRESHOLD:
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=email_1, password=app_password)
        connection.sendmail(
            from_addr=email_1, to_addrs=email_2,
            msg=f"Subject: Price Alert\n\n{message}",
        )
