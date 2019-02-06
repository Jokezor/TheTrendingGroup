'''
    This function takes the period to look for and converts to a date format
    which will be used by Google Trends API.

    Input: period_to_look (string)
    Output: list of date formats (string)
'''

from datetime import date
import Time_funcs

def Period_to_timeframe(period_to_look):
    today = date.today()
    timeframes = []

    if (period_to_look == "Year"):
        last_month = Time_funcs.subtract_one_month(today)

        dates = str(last_month) + " " + str(today)
        timeframes.append(dates)

        for i in range(0,11):
            current_month = last_month
            last_month = Time_funcs.subtract_one_month(current_month)

            dates = str(last_month) + " " + str(current_month)
            timeframes.append(dates)



    '''
    if (period_to_look == "Month"):

    if (period_to_look == "Week"):

    if (period_to_look == "Day"):
    '''

    print(timeframes)
# Test to subtract one Month
#today = date.today()
#print(Time_funcs.subtract_one_month(today))
period_to_look = "Year"
Period_to_timeframe(period_to_look)
