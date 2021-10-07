#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct  7 14:36:12 2021

@author: gillsley
"""
import pandas as pd

class data():
    
    def __init__(self):
        self.df = pd.read_csv('Order_Register.csv', header = 'infer', index_col = 0)
        
    def filterByClient(self, client: str):
        df = self.df
        df = df[df['Name']== client]
        self.df = df


    def filterByPair(self, pair: str):
        df = self.df
        df = df[df['Pair'] == pair]
        self.df = df   


    def filterByTradeType(self, order_type: str):
        df = self.df
        if order_type == 'Buy':
            df = df[df['Order_Size'] > 0]
        elif order_type == 'Sell':
            df = df[df['Order_Size'] < 0]
        else:
            print("Invalid Order Type, must be Buy or Sell")
            
        self.df = df

    def filterByDate(self, date: str):
        df = self.df
        df = df[df['Date'] == date]
        self.df = df
        
    def exportData(self):
        self.df.to_csv('view_export.csv')