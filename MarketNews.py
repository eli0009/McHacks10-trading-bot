import requests
from config import API_KEY, API_SECRET
import json
from Article import Article
from bs4 import BeautifulSoup



def get_articles(API_KEY = API_KEY, API_SECRET = API_SECRET, date = '2023-01-25', symbol:str = "AAPL"):
    headers = {
        'Apca-Api-Key-Id': API_KEY,
        'Apca-Api-Secret-Key': API_SECRET
    }

    params = {'symbols': symbol}

    response = requests.get('https://data.alpaca.markets/v1beta1/news', headers=headers, params=params)

    if response.status_code == 200:
        data = json.loads(response.text)
        articleObjs = Article.read_json_to_articles(data["news"])
        return articleObjs
    else:
        return f'Error: {response.status_code}'


def get_page_text(url):
        # Make a request to the webpage
        response = requests.get(url)
        # Parse the HTML content
        soup = BeautifulSoup(response.content, 'html.parser')
        # Extract the title and text
        title = soup.find('title').get_text()
        text = soup.get_text("\n")
        # Return the title and text as a tuple
        return (title, text)


if __name__ =='__main__':

    articleObjs = get_articles()
    title, text = get_page_text(articleObjs[0].url)
    print(title)
    print(text)
