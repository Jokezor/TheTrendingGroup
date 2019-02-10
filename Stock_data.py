'''
    This program is solely responsable for taking the stock data and output
    a hashtable with the time and stock data.
    we use a module named pandas to read the stock data from google finance

    Input: Company/Companies and timeframe
    Output: Hashtable with dates and hashtable for each company with stock prices
'''

from pandas_datareader import data
import matplotlib.pyplot as plt
import pandas as pd
import datetime
from datetime import date, timedelta
import Time_funcs

from yahoofinancials import YahooFinancials


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

    # 2. Get data for all the tickers

    # 3. Maybe reshape the hashtable?

    # 4. Return the hashtable

    tickers = ['AAPL', 'MSFT', 'GSPC']

    # https://stackoverflow.com/questions/51286525/getting-stock-historical-data-from-api-for-a-python-project

    # First date
    start_date = timeframe[0:10]

    # Second date
    end_date = timeframe[11:len(timeframe)]


    # Select Tickers and stock history dates
    ticker = 'AAPL'
    ticker2 = 'MSFT'
    ticker3 = 'INTC'
    index = '^NDX'
    freq = 'daily'

    # Construct yahoo financials objects for data extraction
    aapl_financials = YahooFinancials(tickers)

    #index_financials = YahooFinancials(index)
    print (aapl_financials.get_historical_price_data(start_date, end_date, freq))#[ticker])


    # Clean returned stock history data and remove dividend events from price history
    daily_aapl_data = clean_stock_data(aapl_financials.get_historical_price_data(start_date, end_date, freq)[ticker]['prices']) #[ticker]['prices'])

    # List of hashtable
    #print(type(daily_aapl_data))

    # Time to construct hashtable from this list.
    '''
    daily_msft_data = clean_stock_data(mfst_financials.get_historical_stock_data(start_date, end_date, freq)[ticker2]['prices'])
    daily_intl_data = clean_stock_data(intl_financials.get_historical_stock_data(start_date, end_date, freq)[ticker3]['prices'])
    #daily_index_data = index_financials.get_historical_stock_data(start_date, end_date, freq)[index]['prices']
    stock_hist_data_list = [{'NDX': daily_index_data}, {'AAPL': daily_aapl_data}, {'MSFT': daily_msft_data}, {'INTL': daily_intl_data}]
    '''


Company = "Apple"
timeframe = "2019-01-08 2019-02-08"


Get_stock_data(Company,timeframe)
