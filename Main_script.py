#!/usr/bin/python
'''
    This is the main script that will call all of the functions.
    We will get the raw data here, send it off to another program to analysis,
    but always get the return value here.

    First we will try to get some trending data from google trends.
'''
#  Imports the Google_data.py program and we can use its functions.
import sys

sys.path.insert(1, '/Users/JO/Documents/TheTrendingGroup/Scripts')

import Google_data
import Benchmark
import Create_files
import Ask_dates
import Period_to_timeframe
import alarm


def main():
    # Asks user and gets all input
    Company, period_to_look, period_of_change, percent_change = Ask_dates.Ask_dates()


    # Reset the companies benchmark files or not
    Reset = False


    # Create new file to store Data
    Create_files.Creation(Company,Reset)


    # Convert period to timeframes for API
    timeframe = Period_to_timeframe.Period_to_timeframe(period_to_look)


    # Calls on the Google_data's function Trending_google with our variables.
    # If not enough data is available, then returns a 0. (int)
    Trend_data = Google_data.Trending_google(Company,timeframe)


    if (Trend_data!=0):
        # Get our benchmarks
        Benchmark.Calc(Trend_data,Company[0]) # Needs to be fixed for list of companies

        # Alarm!
        alarm.Num(Trend_data, Company[0], percent_change, period_of_change)


    else:
        print ("\n \nERROR MESSAGE: No Trending data! \n")
        print ("Trend data:" + str((Trend_data)))
        return 1


if __name__ == "__main__":
    main()
