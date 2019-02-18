'''
    This program is solely responsable for taking the stock data and output
    a hashtable with the stock data.
    we use a module named yahoofinancials to read the stock data

    Input: Company/Companies and timeframe
    Output: Hashtable with hashtable for each company with stock prices
'''

import datetime
from datetime import date, timedelta
import Time_funcs
import Company_to_ticker
import numpy as np
import time
import Time_funcs

from yahoofinancials import YahooFinancials

# https://pypi.org/project/yahoofinancials/

def Get_stock_data(Company,timeframe):
    # Define the instruments to download. We would like to see Apple, Microsoft and the S&P500 index.

    # 1. Convert company names to tickers
    tickers = Company_to_ticker.Company_to_ticker(Company)

    # https://stackoverflow.com/questions/51286525/getting-stock-historical-data-from-api-for-a-python-project

    # First date
    start_date = timeframe[0:10]

    # Second date
    end_date = timeframe[11:len(timeframe)]

    # Frequency of the stock data
    freq = 'daily'

    # Checks if there is a difference of a year
    check_start = start_date.replace("-", "")
    check_end = end_date.replace("-","")
    check_start = (datetime.datetime.strptime(check_start, "%Y%m%d").date())
    check_end = (datetime.datetime.strptime(check_end, "%Y%m%d").date())
    if ((check_end-check_start).days)>=365:
        freq = 'weekly'


    # Create hashtable to store hashtables of company stock data
    Stock_data = {}

    # Go through each companies tickers
    for ticker in tickers:

        # second hashtable to store prices in
        Prices = {}

        # Construct yahoo financials objects for data extraction
        financials = YahooFinancials(ticker)

        finance = financials.get_historical_price_data(start_date, end_date, freq)[ticker]['prices']

        # Create lists
        Open_values = []
        Close_values = []

        # Check if weekno+1 is >=5, then add two ['close'] to both Open_values and Close_values

        # Fixes stock prices for dates of weekends. Need only to check if we have
        # daily data.
        if freq == 'daily':
            weekno = check_start.weekday()

            # First add if the start date is on a weekend
            while (weekno)>=5:
                Open_values.append(finance[0]['open'])
                Close_values.append(finance[0]['close'])
                weekno = (weekno+1)%7

            for i in range(0,len(finance)):
                Open_values.append(finance[i]['open'])
                Close_values.append(finance[i]['close'])
                weekno = (weekno+1)%7
                print(finance[i]['formatted_date'])

                while (weekno)>=5:
                    Open_values.append(finance[i]['close'])
                    Close_values.append(finance[i]['close'])
                    weekno = (weekno+1)%7
        # Just add the data for weekly stock data
        else:
            for i in range(0,len(finance)):
                Open_values.append(finance[i]['open'])
                Close_values.append(finance[i]['close'])


        Prices['open'] = np.array(Open_values)
        Prices['close'] = np.array(Close_values)

        Stock_data[ticker] = Prices

    return Stock_data
