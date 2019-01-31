'''
    This program is solely responsable for taking the stock data and output
    a hashtable with the time and trending data.
    we use a module named pandas to read the stock data from google finance

    Input: Company and timeframe
    Output: Hashtable with the time and corresponding stock data
'''

from pandas_datareader import data
import matplotlib.pyplot as plt
import pandas as pd
from datetime import date

def Get_stock_data(Company,period_to_look):
    # Define the instruments to download. We would like to see Apple, Microsoft and the S&P500 index.
    tickers = ['AAPL', 'MSFT', '^GSPC']

    # What periods do we consider?
    if period_to_look == "Week":
        end_date = str(date.today())

    print(end_date)

    # We would like all available data from 01/01/2000 until 12/31/2016.
    start_date = '2010-01-01'
    end_date = '2016-12-31'

    # User pandas_reader.data.DataReader to load the desired data. As simple as that.
    #panel_data = data.DataReader('INPX', 'google', start_date, end_date)
