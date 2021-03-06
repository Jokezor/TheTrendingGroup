import datetime
import numpy as np
import pandas as pd
import Hashit
# Input: Hashtable - {Array:dtype:object,DatetimeIndex:dtype:datetime64}
#        Company
# Output: Modified files

def Calc(Trend_data,Company):

    File_data = Hashit.Create(Company,Company+"_Bench")
    File_Trend = Hashit.Create(Company,Company+"_Trend")

    if File_Trend == 0:
        pass # Empty file -> New run
    else:
        Scale_factor = sum(Trend_data[Company][0:-2])\
        / sum(File_Trend[Company][1:-1])


    # Find the last element and date from the Data
    Last_element = Trend_data[Company][-1]
    Last_date = Trend_data["Date"][-1]

    # Find the Benchmark date, element and index from the Data
    Bench_index = -1
    for i in range(0,len(Trend_data[Company])):
        if Trend_data[Company][i] > 99.9:
            Bench_index = i
            Bench_element = Trend_data[Company][i]
            Bench_date = Trend_data["Date"][i]
            break
    if Bench_index == -1:
        print("Fatal error in Bench_index")
        print(Trend_data[Company])
        exit()

    # Check if a new run has been made, if yes, store values in Hash Table
    # If no, check if a new Benchmark exist, if yes, store it
    # and overwrite total change
    New_compare = pd.DatetimeIndex(["1970-01-01T00:00:00"])
    if File_data["Date"][0] == New_compare:
        File_data["Date"][0] = Bench_date
        File_data["Date"][1] = Bench_date
        File_data["Date"][2] = Last_date
        File_data[Company][0] = Bench_element
        File_data[Company][1] = Bench_element
        File_data[Company][2] = Last_element
    else:
        Date_compare = pd.DatetimeIndex(File_data["Date"])
        if Date_compare[1] != Bench_date:
            File_data[Company][0] = File_data[Company][0]\
            / Scale_factor
            File_data[Company][1] = Bench_element
            File_data["Date"][1] = Bench_date
            File_data["Date"][2] = Last_date
            File_data[Company][2] = Last_element
        else:
            File_data["Date"][2] = Last_date
            File_data[Company][2] = Last_element

    # Store Hashtables into respective file
    Hashit.Store(Company,Company+"_Bench",File_data)
    Hashit.Store(Company,Company+"_Trend",Trend_data)


    return 0
