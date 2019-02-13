#!/usr/bin/python
'''
    This is the main script that will call all of the functions.
    We will get the raw data here, send it off to another program to analysis,
    but always get the return value here.

    First we will try to get some trending data from google trends.

'''
#  Imports the Google_data.py program and we can use its functions.
#  Comment extra
import Google_data
import Stock_data
import Ask_dates
import Period_to_timeframe

def main():

    # Asks user and gets all input
    #Company, period_to_look, period_of_change, percent_change = Ask_dates.Ask_dates()

    # What company we want to check
    Company = ['Apple Inc.', 'Neonode Inc.']

    # Period to look and take benchmark for
    period_to_look = "Week"

    # Period to check for vs benchmark
    period_of_change = "Day"

    # Percent change for alarm
    percent_change = 10

    # If the user is lazy or not
    auto = 1

    # just fun message output
    #if auto:
    #    print "Auto mode engaged"

    if period_to_look == "Week":
        # Gets the last year's data
        timeframe = "today 1-y"

    # Test to get one dates trending factor
    # Convert period to timeframes for API
    #timeframe = Period_to_timeframe.Period_to_timeframe(period_to_look)
    timeframe = '2019-01-01 2019-02-01'


    # Calls on the Google_data's function Trending_google with our variables.
    # If not enough data is available, then returns a 0. (int)
    #Trend_data = Google_data.Trending_google(Company,timeframe)
    Stock_datas = Stock_data.Get_stock_data(Company,timeframe)

    # Prints the trending data.
    print (Stock_datas)

if __name__ == "__main__":
    main()
