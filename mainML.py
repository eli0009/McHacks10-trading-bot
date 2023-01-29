from model import sentiment
from MarketNews import get_articles, get_page_text, Article
from typing import List

def analyse_news(articleObjs:List[Article]):
    recommendationScore = 0
    for article in articleObjs:
        title, textLines = get_page_text(articleObjs[article].url)
        overall_sentiment, confidence = sentiment(textLines.split("\n"))

        #at this point confidence = recommendation score since we've multiplied it by +-1
        recommendationScore += confidence

    return recommendationScore

def get_stock_prediction(ticker:str, threshold = 0.66):
    articleObjs = get_articles(symbol = ticker)
    recommendationScore = analyse_news(articleObjs)

    buy, hold, sell = 0.66,0,-0.66

    if recommendationScore> buy:
        return 1
    elif recommendationScore < sell:
        return -1
    else:
        return hold
