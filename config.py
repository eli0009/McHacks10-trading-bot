# File paths
credentialsPath = r"tradingBot/credentials/credentials.json"

import json
with open(credentialsPath, 'r') as jsonfile:
    data = json.load(jsonfile)
    USERNAME = data["username"]
    PASSWORD = data["password"]
    API_KEY = data["api_key"]
    API_SECRET = data["api_secret"]

COHERE_KEY = "9jSzWMtL8h77b911YKbf0wdmA9p5xm7NxzRnKDT8"
