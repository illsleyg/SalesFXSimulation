#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct  5 15:29:53 2021

@author: gillsley
"""

import tkinter as tk
from tkinter import ttk
import pandas as pd
from data import data    
    

def MainMenu(df):
    window = tk.Tk()
    window.geometry("500x500")
    window.pack_propagate(False)
    window.resizable(0, 0)
    
    window.title('SVB FX Demo')

    tk.Label(window, text = 'Please Choose one of the following options').pack()
    tk.Button(window, text = 'Data Editor', command= DataEditor(df)).pack()
    tk.Button(window, text = 'Data Visualiser').pack()
    tk.Button(window, text="Quit", command=window.destroy).pack()

    window.mainloop()
    
def DataEditor(df):
    
    windowDE = tk.Tk()
    windowDE.title('Data Editor')
    windowDE.geometry("1000x1000")
    windowDE.pack_propagate(False)
    windowDE.resizable(0,0)
    
    data_frame = tk.LabelFrame(windowDE, text = 'Transaction Data')
    action_frame = tk.LabelFrame(windowDE, text = 'Operators')
    export_frame = tk.LabelFrame(windowDE, text = 'Export')
    
    export_frame.place(height = 100, width = 1000)
    data_frame.place(height = 500, width = 1000)
    action_frame.place(height = 200, width = 1000, rely = 0.65, relx =0)
    
    exp_button = tk.Button(export_frame, text= "Export Data", command = lambda: df.exportData())
    exp_button.place(rely = 0, relx = 0.5)
    
    # Scroll Bar
    tv1 = ttk.Treeview(data_frame)
    tv1.place(relheight = 1, relwidth = 1)
    
    treescrolly = tk.Scrollbar(data_frame, orient = 'vertical', command=tv1.yview)
    treescrollx = tk.Scrollbar(data_frame, orient = 'horizontal', command=tv1.xview)
    tv1.configure(xscrollcommand= treescrollx.set, yscrollcommand=treescrolly.set)
    treescrollx.pack(side = 'bottom', fill = 'x')
    treescrolly.pack(side='right', fill = 'y')
    tv1['column'] = list(df.df.columns)
    tv1['show'] = 'headings'
    
    entry0 = tk.Entry(action_frame)
    entry0.insert(0, 'Client Name')
    entry0.place(rely = 0, relx = 0.2)
    
    entry1 = tk.Entry(action_frame)
    entry1.insert(0, 'Pair Identifier')
    entry1.place(rely = 0.5, relx = 0.2)
    
    entry2 = tk.Entry(action_frame)
    entry2.insert(0, 'OrderType')
    entry2.place(rely = 0, relx = 0.7)
    
    entry3 = tk.Entry(action_frame)
    entry3.insert(0, 'Date')
    entry3.place(rely = 0.5, relx = 0.7)
    
    button = tk.Button(action_frame, text = 'Filter By Client', command = lambda: [df.filterByClient(entry0.get()), DataEditor(df)])
    button.place(rely = 0, relx = 0)
    button1 = tk.Button(action_frame, text = 'Filter By Pair', command = lambda: [df.filterByPair(entry1.get()), DataEditor(df) ])
    button1.place(rely = 0.5, relx = 0)
    button2 = tk.Button(action_frame, text = 'Filter By OrderType', command =  lambda: [df.filterByTradeType(entry2.get()), DataEditor(df)])
    button2.place(rely = 0, relx = 0.5) 
    button3 = tk.Button(action_frame, text = 'Filter By Date', command = lambda: [df.filterByDate(entry3.get()), DataEditor(df)])
    button3.place(rely = 0.5, relx = 0.5)
        
    
    for column in tv1['column']:
        tv1.heading(column, text = column)
        
    df_rows  = df.df.to_numpy().tolist()
    for row in df_rows:
        tv1.insert("", "end", values=row)
    return None
    
  
        
df = data()    
MainMenu(df)