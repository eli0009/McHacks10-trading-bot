import re
import requests
from bs4 import BeautifulSoup
from typing import List, Tuple
import datetime

def get_crypto_news_links(date: str, num_links: int = 30) -> List[str]:
    """
    This function returns a list of links of news articles on cryptography or crypto from Google News
    for a specified date and limits the number of links to the specified number.

    Parameters:
    date (str): The date for which the news articles are to be fetched in the format 'yyyy-mm-dd'
    num_links (int): The number of links to be returned, defaults to 30

    Returns:
    List[str]: A list of links of news articles on cryptography or crypto
    """
    try:
        # check for valid date format
        datetime.datetime.strptime(date, '%Y-%m-%d')
    except ValueError:
        raise ValueError("Incorrect date format, should be 'yyyy-mm-dd'")

    # construct the search query
    query = 'crypto'+ date
    # create the URL
    url = f"https://www.google.com/search?q={query}&tbm=nws"
    # send a GET request
    res = requests.get(url)
    # parse the response
    soup = BeautifulSoup(res.text, 'html.parser')
    # find all the links on the page
    links = soup.find_all('a')
    # filter the links to get only news links
    news_links = [link.get('href') for link in links if '/url?q=' in link.get('href')]
    # return the first num_links links
    return news_links[:num_links]

# Example usage
date = '2022-01-01'
num_links = 20
try:
    news_links = get_crypto_news_links(date, num_links)
    for i in news_links:
        print(i)
except ValueError as e:
    print(e)
