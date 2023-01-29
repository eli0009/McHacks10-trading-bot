import requests
from config import API_KEY, API_SECRET
import json
from test import Article
headers = {
    'Apca-Api-Key-Id': API_KEY,
    'Apca-Api-Secret-Key': API_SECRET
}

# Specify the date for which you want to retrieve news articles
date = '2023-01-25'

# Replace BTC with the desired cryptocurrency symbol
params = {'symbols': 'AAPL'}

response = requests.get('https://data.alpaca.markets/v1beta1/news', headers=headers, params=params)

# print(response)
# Check if the request was successful
if response.status_code == 200:
    # Parse the JSON response
    data = json.loads(response.text)
    articleObjs = Article.read_json_to_articles(data["news"])

    # Print the news articles
    print(articleObjs)
else:
    print(f'Error: {response.status_code}')
