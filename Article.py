from datetime import datetime
import requests
from bs4 import BeautifulSoup

class Article:
    def __init__(self, url, date, headline, symbol):
        self.url = url
        self.date = datetime.strptime(date, r'%Y-%m-%dT%H:%M:%SZ')
        self.headline = headline
        self.symbol = symbol
        self.content = ()

    # @staticmethod
    # def get_page_text(url):
    #     # Make a request to the webpage
    #     response = requests.get(url)
    #     # Parse the HTML content
    #     soup = BeautifulSoup(response.content, 'html.parser')
    #     # Extract the title and text
    #     title = soup.find('title').get_text()
    #     text = soup.get_text()
    #     # Return the title and text as a tuple
    #     return (title, text)

    # def setContent(self, content:tuple):



    def __str__(self):
        return self.headline

    def __repr__(self):
        return f'Article(url={self.url}, date={self.date}, headline={self.headline}, symbol={self.symbol})'

    @classmethod
    def read_json_to_articles(cls,jsonFile) -> list:
        articles = []
        data = jsonFile
        for item in data:
            articles.append(Article(item['url'], item['created_at'], item['headline'], item['symbols']))
        return articles
