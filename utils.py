#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 29 20:40:43 2021

@author: gillsley
"""

import random
import string
import pandas as pd
from datetime import date


def getClientName():
    clientName = ""
    for x in range(4):
        letter_choice = random.choice(string.ascii_uppercase)
        clientName = clientName + letter_choice
    
    return clientName

def getDateRange():
    datelist = pd.date_range(date.today(), periods=365).tolist()
    
    return datelist
