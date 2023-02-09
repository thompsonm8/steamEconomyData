#Credit to https://www.blakeporterneuro.com/learning-python-project-3-scrapping-data-from-steams-community-market/ for tutorial on setting this up

import requests
import json
import pickle

import pandas as pd
import numpy as np
import scipy.stats as sci

from datetime import datetime
import time

loginCredentials = {'steamLoginSecure': 'cookie!(personal data not adding my own cookie for safety)'}
games = [730, 440] # [CSGO, TF2]

# Grab Items
for gameID in games:
    itemNames = []

    # total number of items 
    itemsGet = requests.get(f'https://steamcommunity.com/market/search/render/?search_descriptions=0&sort_column=default&sort_dir=desc&appid={gameID}&norender=1&count=100', cookies=loginCredentials)
    items = itemsGet.content
    items = json.loads(items)
    totalItems = items['total_count']

    # Limited to getting 100 items per try
    for x in range(0,totalItems+50,50): # Looping multiple times to get all of the items due to the 100 per try constraint
        time.sleep(2.5) # Can't make too many requests in a short period of time

        itemGet = requests.get(f'https://steamcommunity.com/market/search/render/?start={str(x)}&count=100&search_descriptions=0&sort_column=default&sort_dir=desc&appid={gameID}&norender=1&count=5000', cookies=loginCredentials)
        print(f"{x}/{totalItems}, Status Code:{itemsGet.status_code}")