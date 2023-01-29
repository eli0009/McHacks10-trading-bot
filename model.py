import cohere
from cohere.classify import Example
from config import COHERE_KEY
from typing import List
co = cohere.Client(COHERE_KEY)


def sentiment(input:List[str]):
  classifications = co.classify(
    model="9dad2d66-6da3-4aff-8812-73a58cce7e99-ft",
    inputs=input
    # ,examples=[Example("The order came 5 days early", "positive"),
    #           Example("AAPL exceeded my expectations", "positive"),
    #           Example("I ordered more for my friends", "positive"),
    #            Example("I would buy AMZM again", "positive"),
    #            Example("I would not recommend this to others", "negative"),
    #            Example("The package from FB was damaged", "negative")]
              )
  print('The confidence levels of the labels are: {}'.format(
        classifications.classifications))

  conclusion = 0
  n = len(classifications.classifications)
  for classification in classifications.classifications:
    if classification.prediction == "positive":
      conclusion += classification.confidence/n
    elif classification.prediction == "negative":
      conclusion -= classification.confidence/n

  return ("positive", conclusion) if conclusion >= 0  else ("negative",conclusion)



if __name__ == "__main__":
  ans = sentiment(["Apple accounted for nearly 24% of China's smartphone sales in the last three months of 2022, according to Counterpoint Research",
                    ".","\n",
                    "In 2022, vivo retained the first spot with a 19.2% market share, followed by Apple at 18.0% and OPPO at 17.5%."])
  print(ans)
  for i in ans:
    print(i)
