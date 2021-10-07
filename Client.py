#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 29 18:22:54 2021

@author: gillsley
"""
import random
import pandas as pd

class client:
    def __init__(self, name):
        
        self.name = name
        self.size = random.randint(0,2) # Defines Tier of company, a simple way of defining market cap
        region_int = random.randint(0,1)
        regions = ["US", "EMEA"]
        self.region = regions[region_int]
        
    def selectFXPair(self):
        """

        Returns
        -------
        pair_traded : STR
            Currency Pair that the company will place an order on.

        """
        
        pair_int = random.randint(0,2)
        pairs_emea = ["EUR/USD", "EUR/GBP", "GBP/USD"]
        pairs_us = ["EUR/USD", "AUD/USD", "USD/CAD"]
        
        if self.region == "US":
            pair_traded = pairs_us[pair_int]
        elif self.region == "EMEA":
            pair_traded = pairs_emea[pair_int]
            
        return pair_traded
    
    def selectSpotSize(self):
            
        if self.size == 0:
            a = 4000
            b = 10000
        elif self.size == 1:
            a = 8000
            b = 50000
        elif self.size == 2:
            a = 45000
            b = 100000
            
        orderSize = random.randint(a, b)
        
        buy_or_sell = random.randint(0, 1)
        if buy_or_sell == 0:
            orderSize = orderSize * -1
        
        return orderSize
        
    def placeSpotOrder(self, pair, orderSize, dates):
        
        order_data = {"Name":[self.name], "Pair": [pair], "Order_Size": [orderSize], 'Date' : [dates]}
        
        order = pd.DataFrame(data = order_data)
        
        return order_data