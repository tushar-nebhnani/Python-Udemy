import os
import csv
from datetime import datetime
import requests
import time
import schedule
import sqlite3

API_URL = "https://api.coingecko.com/api/v3/coins/markets"
PARAMS = {
    'vs_currency': 'inr',
    'order': 'market_cap_desc',
    'per_page': 10,
    'page': 1,
    'sparkline': False,
}
DB_NAME = "crypto.db"

def fetch_crypto_data():
    response = requests.get(API_URL, params=PARAMS)
    return response.json()

def create_table():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute('''
            CREATE TABLE IF NOT EXISTS crypto_prices (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                timestamp TEXT,
                coin TEXT,
                price REAL
            )
    ''')
    conn.commit()
    conn.close()

def save_to_db(data):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    for coin in data:
        cursor.execute('''
                INSERT INTO crypto_prices(timestamp, coin, price) VALUES(?, ?, ?)
    ''',(timestamp, coin['id'], coin['current_price']))
    conn.commit()
    conn.close()
    print("Price Saved to Database.")
    
def search_coin(coin_name):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute('''
            SELECT timestamp, price FROM crypto_prices
                   WHERE coin = ?
                   ORDER BY timestamp DESC
                   LIMIT 1
    
    ''', (coin_name,))
    result = cursor.fetchone()
    conn.close()
    # print("Raw Result: ", result)/
    if result:
        print(f"${result[1]}")


def main():
    create_table()
    print("1. Fetch and store\n2. Search latest price")
    choice = input("Choose an option: ").strip()

    if choice == '1':
        data = fetch_crypto_data()
        save_to_db(data)
    elif choice == '2':
        coin_name = input("Enter coin name: ").strip().lower()
        search_coin(coin_name)
    else:
        print("Invalid Option.")

main()