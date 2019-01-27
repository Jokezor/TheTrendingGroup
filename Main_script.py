#!/usr/bin/python
'''
    This is the main script that will call all of the functions.
    We will get the raw data here, send it off to another program to analysis,
    but always get the return value here.

    First we will try to get some trending data from google trends.

'''
import subprocess
import os

def main():

    # What company we want to check
    Company = '"NeoNode"'

    # Gets the last hourly data
    timeframe = '"now 7-d"'

    # Get google data, Trending_google captures the print() from Google_data.py
    Trending_google = subprocess.check_output("python Google_data.py " + Company + " " + timeframe, shell=True, stderr=subprocess.STDOUT)

    # Currently is a string. Need to find a way to return list instead of string.
    print (Trending_google)

main()
