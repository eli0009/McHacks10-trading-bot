from model import sentiment
from MarketNews import get_articles, get_page_text, Article
from typing import List

def analyse_news(articleObjs:List[Article]):
    recommendationScore = 0
    for article in articleObjs:
        print(article)
        title, textLines = get_page_text(article.url)
        textLines.append(title)
        recommendationScore = sentiment(textLines)
        print("Done")

    return recommendationScore

def get_stock_prediction(ticker:str, threshold = 0.66):
    articleObjs = get_articles(symbol = ticker)
    recommendationScore = analyse_news(articleObjs)

    buy, hold, sell = threshold, 0, -threshold

    if recommendationScore> buy:
        return 1
    elif recommendationScore < sell:
        return -1
    else:
        return hold



if __name__ == "__main__":
    stock = input("Pleae enter a large cap US Equity Symbol (ex: AAPL): ").upper()
    decision = get_stock_prediction(stock)
    print(decision)
