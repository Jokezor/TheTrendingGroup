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

from yahoofinancials import YahooFinancials

# https://pypi.org/project/yahoofinancials/

# Function to clean data extracts
def clean_stock_data(stock_data_list):
    new_list = []
    for rec in stock_data_list:
        if 'type' not in rec.keys():
            new_list.append(rec)
    return new_list


def Get_stock_data(Company,timeframe):
    # Define the instruments to download. We would like to see Apple, Microsoft and the S&P500 index.

    # 1. Convert company names to tickers
    tickers = Company_to_ticker.Company_to_ticker(Company)

    # Frequency of the stock data
    freq = 'daily'

    # https://stackoverflow.com/questions/51286525/getting-stock-historical-data-from-api-for-a-python-project

    # First date
    start_date = timeframe[0:10]

    # Second date
    end_date = timeframe[11:len(timeframe)]

    # Create hashtable to store hashtables of company stock data
    Stock_data = {}

    # Go through each companies tickers
    for ticker in tickers:

        # second hashtable to store prices in
        Prices = {}

        # Construct yahoo financials objects for data extraction
        aapl_financials = YahooFinancials(ticker)

        Open_values = []
        for day in aapl_financials.get_historical_price_data(start_date, end_date, freq)[ticker]['prices']:
            Open_values.append(day['open'])


        Close_values = []
        for day in aapl_financials.get_historical_price_data(start_date, end_date, freq)[ticker]['prices']:
            Close_values.append(day['close'])

        Prices['open'] = Open_values
        Prices['close'] = Close_values

        Stock_data[ticker] = Prices


    return Stock_data
