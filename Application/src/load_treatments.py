import os
import json

# read treatments from json
def get_treatments():
    if os.path.exists("./json/treatments/treatments.json"):
        try:
            with open("./json/treatments/treatments.json") as file:
                return json.load(file)
        except json.JSONDecodeError:
            return {}
    else:
        return {}

# update treatments json
def save_treatments(treatments):
    if os.path.exists("./json/treatments/treatments.json"):
        try:
            with open("./json/treatments/treatments.json", 'w') as file:
                json.dump(treatments, file, indent=4)
        except json.JSONDecodeError:
            return {}
