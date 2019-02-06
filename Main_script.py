#!/usr/bin/python
'''
    This is the main script that will call all of the functions.
    We will get the raw data here, send it off to another program to analysis,
    but always get the return value here.

    First we will try to get some trending data from google trends.

'''
import subprocess
import os
import Google_data # Imports the Google_data.py program and we can use its functions.


def main():

    # What company we want to check
    Company = ["NeoNode", "Apple", "IBM", "Hoka one one"]

    # Gets the last week's data
    timeframe = "now 7-d"


    i = 0;
    for i in  range(0, len(Company)):
        # Calls on the Google_data's function Trending_google with our variables.
        Trend_data = Google_data.Trending_google(Company[i], timeframe)

        # Prints the trending data.
        print (Trend_data)

    # This line is not necessery.
if __name__ == "__main__":
    main()
