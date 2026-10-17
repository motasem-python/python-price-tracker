"""
Price Tracker by Motasem Mostafa
Tracks product prices and alerts when price drops.
"""

import requests
from bs4 import BeautifulSoup
from datetime import datetime

# Config - Change this to any product you want
PRODUCT_URL = "https://www.amazon.com/dp/B075CY5MY8"
TARGET_PRICE = 300.0

HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36",
    "Accept-Language": "en-US,en;q=0.9"
}

def check_price():
    try:
        print(f"[{datetime.now()}] Checking price for product...")
        print(f"URL: {PRODUCT_URL}")
        print(f"Target: ${TARGET_PRICE}")
        
        # For demo - in real project we parse the page
        # response = requests.get(PRODUCT_URL, headers=HEADERS)
        # soup = BeautifulSoup(response.content, 'html.parser')
        
        current_price = 249.99  # Simulated price
        print(f"Current Price: ${current_price}")
        
        return current_price
    except Exception as e:
        print(f"Error: {e}")
        return None

def send_alert(price):
    print(f"🚨 ALERT! Price dropped to ${price} - Sending notification!")

if __name__ == "__main__":
    price = check_price()
    if price and price < TARGET_PRICE:
        send_alert(price)
    else:
        print("Price is still high. Will check again later.")
