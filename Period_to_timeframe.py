'''
    This function takes the period to look for and converts to a date format
    which will be used by Google Trends API.

    Input: period_to_look (string)
    Output: date format (string)
'''

from datetime import date
from datetime import timedelta

import Time_funcs

def Period_to_timeframe(period_to_look):
    today = date.today()

    if (period_to_look == "Year"):
        last_month = Time_funcs.subtract_one_month(today)

        dates = str(last_month) + " " + str(today)
        timeframe=dates

        for i in range(0,11):
            current_month = last_month
            last_month = Time_funcs.subtract_one_month(current_month)

            dates = str(last_month) + " " + str(current_month)
        dates = str(last_month) + " " + str(today)
        print(dates)
        timeframe=dates

    if (period_to_look == "Month"):

        last_month = Time_funcs.subtract_one_month(today)
        dates = str(last_month) + " " + str(today)

        print(dates)
        timeframe=dates

    if (period_to_look == "Week"):
        last_week = date.today() - timedelta(days=7)
        timeframe = str(last_week) + " " + str(today)
        print(timeframe)

    if (period_to_look == "Day"):
        last_day = date.today() - timedelta(days=1)
        timeframe = str(last_day) + " " + str(today)
        print(timeframe)


# Test to subtract one Month
#today = date.today()
#print(Time_funcs.subtract_one_month(today))
period_to_look = "Day"
Period_to_timeframe(period_to_look)
