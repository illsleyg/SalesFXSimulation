# SalesFXSimulation

Simulation Parameters

To create sample data an oversimplified simulation was run to create a basic order register which would list each trade placed by a simulated client, the trade size in units, the currency pair traded, and the date of the transaction.

To simulate a very simple client portfolio we have used Python to create a portfolio of 100 clients. These clients belong to one of two regions, US or EMEA which are assigned randomly. The region each client belongs to determines which currency pairs they are interested in trading, with US clients focused on "EUR/USD", "AUD/USD" and "USD/CAD" whilst EMEA clients primarily trade in 
EUR/USD", "EUR/GBP" and "GBP/USD". For simplicity all trading was spot trades. Each client is also assigned a company size which can either be Tier 1, Tier 2, or Tier 3, which could be likened to market cap and determines the size of a spot trade the client will make.  

The simulation was run over 365 days, with each client placing between 1 – 30 trades per day. The clients have the randomly chosen option to either buy or sell a currency pair. 

The flaw of the model is that it is in a randomly distributed environment, where trends and market events that can cause a bullish or bearish trend are not simulated. The aim is to understand which clients are moving money where and allowing the Market risk solutions team

The simulations were made up of three .py files 
•	Client - which defines the client class and parameters (eg.name, size, region) and allows them to place trades, determines the size of a trade and whether that would be a buy or sell action. 
•	Utils – which contains a number of functions to assist with the running of the simulation.
•	Main – Consolidates functions and classes from other files and runs the simulations.

Each Client is given a Name, Region, Size 
	Each Client is given a randomly assigned ticker (Random 4 Letter Code) to allow us to differentiate between clients. 
	Each Client is given a region, US or EMEA which determines which currency pairs it is primarily interested in trading in.
	Each Client is given a size, Tiers 1-3, and these determine the size of potential trades, with Tiers 3 making the largest trades by units
