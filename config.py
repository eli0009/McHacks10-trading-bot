# File paths
import os
import json

current_directory = os.getcwd()
credentialsPath = current_directory + r"\credentials\credentials.json"

attempts = 0
while attempts < 2:

    try:
        with open(credentialsPath, 'r') as jsonfile:
            data = json.load(jsonfile)
            USERNAME = data["username"]
            PASSWORD = data["password"]
            API_KEY = data["api_key"]
            API_SECRET = data["api_secret"]
        break
    except FileNotFoundError:
        attempts += 1
        credentialsPath = current_directory + r"\trading-bot2\credentials\credentials.json"


COHERE_KEY = "9jSzWMtL8h77b911YKbf0wdmA9p5xm7NxzRnKDT8"
