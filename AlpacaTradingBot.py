#!/usr/bin/env python
# coding: utf-8

# # Inputs

# In[8]:


# File paths
credentialsPath = "./credentials/credentials.json"


# # Imports

# In[9]:


import json

# Importing the API
from alpaca.trading.client import TradingClient


# # Creating Trading Client

# In[10]:


# Instantiating the REST client according to the keys
with open(credentialsPath, 'r') as jsonfile:
    data = json.load(jsonfile)
    USERNAME = data["username"]
    PASSWORD = data["password"]
    API_KEY = data["api_key"]
    API_SECRET = data["api_secret"]

#Creating a paper trading client
trading_client = TradingClient(API_KEY, API_SECRET, paper=True)


# Buying power can be found inside one’s account information. Use the get_account method on the trading client and print the result to show your account information.

# In[11]:


account = trading_client.get_account()



# In[20]:
""" Methods """
def printAccountProperties():
    for property_name, value in account:
        print(f"\"{property_name}\": {value}")
        
# Get all open positions and print each of them
def getAllPositions():
    print("Getting Positions")

    positions = trading_client.get_all_positions()
    if not positions:
        print("None")
        return

    for position in positions:
        for property_name, value in position:
            print(f"\"{property_name}\": {value}")

    print("Done")
