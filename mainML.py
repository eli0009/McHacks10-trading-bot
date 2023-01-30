from model import sentiment
from MarketNews import get_articles, get_page_text, Article
from typing import List

def analyse_news(articleObjs:List[Article], a = ""):
    recommendationScore = 0

    if a :
        print('Processing all titles...')
        textLines = [get_page_text(article.url)[0] for article in articleObjs]
        recommendationScore = sentiment(textLines)
        print("Done!")
    else:
        for article in articleObjs:
            print(f"Analysing article:{article}...")
            title, textLines = get_page_text(article.url)
            if a !="":
                textLines = []
            textLines.append(title)
            recommendationScore = sentiment(textLines)
            print("Done")

    return recommendationScore

def get_stock_prediction(ticker:str, threshold = 0.66, a= "" ):
    articleObjs = get_articles(symbol = ticker)
    recommendationScore = analyse_news(articleObjs, a)

    buy, hold, sell = threshold, 0, (-1*threshold)

    if recommendationScore> buy:
        return "Buy\n"
    elif recommendationScore < sell:
        return "Sell\n"
    else:
        return "Hold\n"



if __name__ == "__main__":
    while input != 'q':
        print("Hit q to quit")
        stock = ""
        attempts = 0
        while not stock and attempts < 2:
            stock = input("Pleae enter a large cap US Equity Symbol (ex: AAPL): ").upper()
            if stock: attempts = 0
            else: attempts +=1

        a = input("Fast version (hit any key for yes/just hit enter for no)?")
        decision = get_stock_prediction(stock,a = a)
        print(decision)
