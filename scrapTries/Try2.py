import requests
from bs4 import BeautifulSoup

# Make a request to the Google News website
url = "https://news.google.com/search?q=crypto&hl=en-US&gl=US&ceid=US%3Aen"
response = requests.get(url)

# Parse the HTML content
soup = BeautifulSoup(response.content, "html.parser")

# Find the news articles on the page
articles = soup.find_all("a", class_="DY5T1d")

print(articles[0])
# # Iterate through the articles and print the headline and summary
# for article in articles:
#     headline = article.find("h3").text
#     summary = article.find("p").text
#     print(headline)
#     print(summary)
#     print()
