'''
    This program is solely responsable for taking the stock data and output
    a hashtable with the stock data.
    we use a module named yahoofinancials to read the stock data
    The stock data gives the data including the start_date
    until the end_date. [start_date,end_date)

    Input: Company/Companies and timeframe
    Output: Hashtable with hashtable for each company with stock prices and dates
    (We need this to debug)
'''

from dateutil import parser
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
    tickers, Closed_days = Company_to_ticker.Company_to_ticker(Company)

    # https://stackoverflow.com/questions/51286525/getting-stock-historical-data-from-api-for-a-python-project

    # First date
    start_date = timeframe[0:10]

    # Second date, checks if we got time dependency
    if len(timeframe)>=25:
        end_date = timeframe[14:len(timeframe)-3]
    else:
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

    # Need to add one more day to the end_date since the API doesn't pull data for the end date.
    check_end = check_end + timedelta(days=1)

    # Create hashtable to store hashtables of company stock data
    Stock_data = {}

    # Go through each companies tickers
    for ticker in tickers:

        # second hashtable to store prices in
        Prices = {}

        # Construct yahoo financials objects for data extraction
        financials = YahooFinancials(ticker)

        # Need to convert datetime to string for API
        finance = financials.get_historical_price_data(start_date, str(check_end), freq)[ticker]['prices']

        # Create lists
        Open_values = []
        Close_values = []

        # Create empty list to ensure we can have companies in different markets combined.
        Dates = []

        # Check if weekno+1 is >=5, then add two ['close'] to both Open_values and Close_values
        # Fixes stock prices for dates of weekends. Need only to check if we have
        # daily data.
        if freq == 'daily':
            weekno = check_start.weekday()
            today = check_start

            # First add if the start date is on a weekend
            while (weekno)>=5:
                Open_values.append(finance[0]['open'])
                Close_values.append(finance[0]['close'])
                Dates.append(today)
                today = today+timedelta(days=1)
                weekno = (weekno+1)%7

            # If we start to check on a holiday, wee need to get the stock info
            # Checks if today is a holiday and if today is a weekend, then
            # we dont need to check since the market is closed
            holiday=1
            while (holiday==1):
                if ((today.strftime('%m') + '-' + today.strftime('%d')) in Closed_days[today.strftime('%Y')] and today.weekday() < 5):
                    Open_values.append(finance[0]['open'])
                    Close_values.append(finance[0]['close'])
                    Dates.append(today)
                    today = today+timedelta(days=1)
                    weekno = (weekno+1)%7
                else:
                    holiday=0

            # Now goes through each financial day
            last_day = []
            for i in range(0,len(finance)):

                today = (finance[i]['formatted_date'])
                today = (datetime.datetime.strptime(today, "%Y-%m-%d").date())

                # Need to check so we don't add the same day's values.
                # YahooFinancials returns two dates, probably something with
                # Closed market values, can't find info on it.
                if (str(today) not in last_day):

                    last_day.append(str(today))
                    Open_values.append(finance[i]['open'])
                    Close_values.append(finance[i]['close'])

                    Dates.append(today)
                    weekno = (weekno+1)%7

                    today = today + timedelta(days=1)

                    # If there's a weekend
                    while (weekno>=5 and today<check_end):
                        Open_values.append(finance[i]['close'])
                        Close_values.append(finance[i]['close'])
                        Dates.append(today)
                        today = today + timedelta(days=1) # Add one day to keep track
                        weekno = (weekno+1)%7

                    # Checks five days ahead if theres holidays on all days in a series
                    # If tomorrow is a holiday then only need to check 5 days more
                    # If there's a non holiday, then stop checking
                    # If we start to check on a holiday, wee need to get the stock info
                    holiday=1
                    while (holiday==1):
                        if ((today.strftime('%m') + '-' + today.strftime('%d')) in Closed_days[today.strftime('%Y')] and weekno <5 and today<check_end):
                            Open_values.append(finance[i]['open'])
                            Close_values.append(finance[i]['close'])
                            Dates.append(today)
                            today = today+timedelta(days=1)
                            weekno = (weekno+1)%7
                        else:
                            holiday = 0

        # Just add the data for weekly stock data
        else:
            # Skip first since yahoo gives the trend leading up the date
            # And google data gives the summary of the week every sunday.
            for i in range(1,len(finance)):
                Open_values.append(finance[i]['open'])
                Close_values.append(finance[i]['close'])
                today = (finance[i]['formatted_date'])
                today = (datetime.datetime.strptime(today, "%Y-%m-%d").date())
                Dates.append(today)

            # If the end date of the timeframe is a sunday, since we added one day
            # to get the data including the end_date, this is equivalent to
            # check_end is a monday.
            if check_end.weekday()==0:
                # Now we need to back until monday and then sum all the closing prices
                # and divide by the amount of days.
                # Get daily data
                #print type(today)
                #print type(start_date)
                freq = 'daily'
                finance = financials.get_historical_price_data(str(today), str(check_end), freq)[ticker]['prices']
                print(finance['formatted_date'])


        Prices['open'] = np.array(Open_values)
        Prices['close'] = np.array(Close_values)

        Stock_data[ticker] = Prices
        Stock_data[ticker]['Date'] = Dates

    return Stock_data
