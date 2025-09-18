import json
import os 

INPUT_FILE = "nested_data.json"
OUTPUT_FILE = "flatten_data.json"

def flatten_json(data, parent_key='', sep = "."):
    items = {}
    
