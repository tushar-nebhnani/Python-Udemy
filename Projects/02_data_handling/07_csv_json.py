"""
    CSV TO JSON
"""

import os
import json
import csv 

INPUT_FILE = 'weather_logs.csv'
OUTPUT_FILE = 'weather_logs_json.json'

def load_csv(filename):
    if not os.path.exists(filename):
        print("No data to read.")
        return
    
    with open(filename, 'r', encoding="utf-8") as f:
        reader = csv.DictReader(f)
        data = list(reader)
        return data
    

def save_json(data, filename):
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2)
    print(f"✅Converted {len(data)} records to {filename}.")

def preview_data(data, count=3):
    for row in data[:count]:
        print(json.dumps(row, indent=2))

def main():
    data = load_csv(INPUT_FILE)
    if not data:
        return
    save_json(data, OUTPUT_FILE)
    preview_data(data, 3)

if __name__ == "__main__":
    main()