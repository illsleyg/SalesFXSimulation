#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct  5 15:12:20 2021

@author: gillsley
"""
import pandas as pd

def filterByClient(df: pd.DataFrame, client: str):
    df = df[df['Name']== client]
    
    return df 

def filterByPair(df: pd.DataFrame(), pair: str):
    df = df[df['Pair'] == pair]
    
    return df

def filterByTradeType(df: pd.DataFrame(), order_type: str):
    if order_type == 'Buy':
        df = df[df['Order_Size'] > 0]
    elif order_type == 'Sell':
        df = df[df['Order_Size'] < 0]
    else:
        print("Invalid Order Type, must be Buy or Sell")
        
    return df

def filterByDate(df: pd.DataFrame(), date: str):
    df = df[df['Date'] == date]
    
    return df