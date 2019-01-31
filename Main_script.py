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

def main():

    #Company, period_to_look, period_of_change, percent_change = Ask_dates.Ask_dates()
    Company = Ask_dates.Ask_dates()
    # What company we want to check
    #Company = "Apple"

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
        # Gets the last week's data
        timeframe = "today 5-y"

    # Test to get one dates trending factor
    timeframe = '2018-12-14 2018-12-15'

    # Calls on the Google_data's function Trending_google with our variables.
    #Trend_data = Google_data.Trending_google(Company,timeframe)
    #Stocks_data = Stock_data.Get_stock_data(Company,period_to_look)

    # Prints the trending data.
    print (Company)

if __name__ == "__main__":
    main()
