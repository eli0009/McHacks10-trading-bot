from flask import Flask, request, render_template
from model import sentiment
from MarketNews import get_articles, get_page_text, Article
from typing import List

app = Flask(__name__)

def analyse_news(articleObjs:List[Article]):
    recommendationScore = 0
    for article in articleObjs:
        title, textLines = get_page_text(article.url)
        textLines.append(title)
        recommendationScore = sentiment(textLines)

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

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        ticker = request.form["ticker"].upper()
        decision = get_stock_prediction(ticker)
        return render_template("index.html", decision=decision)
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True, port = 80)
