import yfinance as yf
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df_yahoo = yf.download("BTC-USD", start="2020-09-15", end="2020-11-15", progress=False)
print(df_yahoo)
