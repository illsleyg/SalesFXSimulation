#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 29 20:39:51 2021

@author: gillsley
"""

from Client import client
from utils import getClientName, getDateRange
import pandas as pd
import random
from datetime import date

def createPortfolio():
    portfolio = []
    for x in range(100):
        name = getClientName()
        portfolio.append(client(name))
        
    return portfolio
        
portfolio = createPortfolio()
date_range = getDateRange()
order_register = pd.DataFrame()

for date in date_range:
    for obj in portfolio:
        no_trades = random.randint(1, 30)
        
        for trades in range(no_trades):
            pair = obj.selectFXPair()
            orderSize = obj.selectSpotSize()
            raw_date = date.date()
            order_receipt = obj.placeSpotOrder(pair, orderSize, raw_date)
            order_register = order_register.append(order_receipt, ignore_index= True)
            if orderSize > 0:
                print("Date - ", raw_date,"TRADE ALERT:", obj.name, "places BUY order of ", orderSize,"into pair", pair)
            if orderSize < 0:
                print("Date - ", raw_date,"TRADE ALERT:", obj.name, "places SELL Order of ", orderSize * -1,"into pair", pair)

for col in order_register.columns:
    order_register[col] = order_register[col].str.get(0)