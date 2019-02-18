#!/usr/bin/python
'''
    This is the main script that will call all of the functions.
    We will get the raw data here, send it off to another program to analysis,
    but always get the return value here.

    First we will try to get some trending data from google trends.

'''
#  Imports the Google_data.py program and we can use its functions.
<<<<<<< HEAD
# Comment extra
=======
#  Comment extra
>>>>>>> 88d98b3f3dc07fe87995b72bac1ee7553ced7083
import Google_data
import Benchmark
import Create_files
import Hashit

def main():


    # What company we want to check
    Company = ["Neonode","Apple"]
    Reset = False

    # Create new file to store Data
    Create_files.Creation(Company,Reset)

    # Period to look and take benchmark for
    period_to_look = "Week"

    # Period to check for vs benchmark
    period_of_change = "Day"

    # Percent change for alarm
    percent_change = 10

    # If the user is lazy or not
    auto = 1

    # just fun message output
    if auto:
        print ("Auto mode engaged")

    if period_to_look == "Week":
        # Gets the last week's data
        timeframe = "today 5-y"

    # Calls on the Google_data's function Trending_google with our variables.
    timeframe = '2019-01-01 2019-02-01'
    Trend_data = Google_data.Trending_google(Company,"now 7-d")
    #Trend_data = Google_data.Trending_google(Company,timeframe)

    # prints the trending data.
    # print (Trend_data)
    #dict = Hashit.Create(Company+"_Trend")

    for comp in Company:
        Changes = Benchmark.Calc(Trend_data,comp)



if __name__ == "__main__":
    main()
