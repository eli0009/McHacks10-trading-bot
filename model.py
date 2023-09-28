import cohere
from cohere.classify import Example
from config import COHERE_KEY
from typing import List
import yfinance as yf
import re

co = cohere.Client(COHERE_KEY)


# To improve runtime, filter out all strings that do not contain the company name nor the ticker
def clean_inputs(input: List[str], ticker:str):
  longName = yf.Ticker(ticker).info['longName']
  cleaned = []
  for string in input:
    if re.search(f"({longName})|({ticker})",string):




def sentiment(input:List[str]) -> float:
  # Call custom model from cohere
  classifications = co.classify(
    model="9dad2d66-6da3-4aff-8812-73a58cce7e99-ft",
    inputs=input)

  #determine recommendationScore of the inputs
  k = len(classifications.classifications)
  for classification in classifications.classifications:
    if classification.prediction == "positive":
      recommendationScore += classification.confidence/k
    elif classification.prediction == "negative":
      recommendationScore -= classification.confidence/k

  return recommendationScore

def sentiment(input:List[str]):
  n = 0
  m = 0
  recommendationScore = 0
  while n < len(input):

    m += min(95, len(input) - n)
    if len(input[n:m]) != 0:

      classifications = co.classify(
          model="9dad2d66-6da3-4aff-8812-73a58cce7e99-ft",
          inputs=input[n:m])

      k = len(classifications.classifications)
      for classification in classifications.classifications:
        if classification.prediction == "positive":
          recommendationScore += classification.confidence/k
        elif classification.prediction == "negative":
          recommendationScore -= classification.confidence/k

    n += m

  def topic_check(sentences:List[str], ticker):
    pass

  # print('The confidence levels of the labels are: {}'.format(
  #       classifications.classifications))






if __name__ == "__main__":
  ans = sentiment(["Apple accounted for nearly 24% of China's smartphone sales in the last three months of 2022, according to Counterpoint Research",
                    ".","\n",
                    "In 2022, vivo retained the first spot with a 19.2% market share, followed by Apple at 18.0% and OPPO at 17.5%."])
  print(ans)
  for i in ans:
    print(i)
