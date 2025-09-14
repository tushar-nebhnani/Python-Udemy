"""
    Real-time weather data CLI
    Bug: API key is wrong> URl is fine
"""
import os 
import csv 
from datetime import datetime
import requests
from dotenv import load_dotenv

load_dotenv()
FILENAME = "weather_logs.csv"
API_KEY = os.getenv('API_KEY')

if not os.path.exists(FILENAME):
    with open(FILENAME, 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(["Date", "City", "Tempreature", "Condition", "Description"])

def log_weather():
    city = input("Enter your city name: ").strip().lower()
    date = datetime.now().strftime("%Y-%m-%d")

    with open(FILENAME, 'r', newline='', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            if row['Date'] == date and row['City'].lower() == city.lower():
                print("Entry for this city and date exists")
                return
    print(API_KEY)
    try:
        URL = f"https://api.openweathermap.org/data/2.5/forecast?q={city}&appid={API_KEY}&units=metric"
        response = requests.get(URL)
        response.raise_for_status()
        data = response.json()

        if response.status_code != 200:
            print(f"Invalid API reponse - ERROR")
            return
        
        temp = data['main']['temp']
        condition = data['weather'][0]['main']
        description = data['weather'][0]['description']

        with open(FILENAME, 'w', newline='', encoding='utf-8') as f:
            writer = csv.writer(f)
            writer.writerow([date, city.title(), temp, condition, description])

            print(f"Logged: {temp} | {condition} | {description} for the city: {city}")

    except Exception as e:
        print("Failed to make API call.")

def view_log():
    with open(FILENAME, 'r', encoding='utf-8') as f:
        reader = list(csv.reader(f))
        if len(reader) <= 1:
            print("No new entries.")
            return
        
        for row in reader[1:]:
            print(f"{row[0]} : {row[1]} : {row[2]} : {row[3]} : {row[4]}")

def main():
    while True:
        print("Real Time Weather Logger")
        print("1. Add weather log")
        print("2. View weather log")
        
        choice = input("Choose an option: ").strip()

        match choice:
            case "1": log_weather()
            case "2": view_log()
            case "3": break

if __name__ == "__main__":
    main()