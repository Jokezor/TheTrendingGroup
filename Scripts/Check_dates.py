'''
    This script will check if the time period specified is acceptable and then adjust
    the timeframe.

    Input: timeframe (string)
    Output: timeframe (string)

'''

import datetime
from datetime import date, timedelta

def Check_dates(timeframe):

    # Check if the date is within 3 days from current date
    end_date = timeframe[11:len(timeframe)]
    start_date = timeframe[0:10]
    check_end = (datetime.datetime.strptime(end_date, "%Y-%m-%d").date())
    check_start = (datetime.datetime.strptime(start_date, "%Y-%m-%d").date())

    if (check_end > date.today()):
        print("Can't check into days that haven't passed.")
    else:
        if (check_end + timedelta(days=2)) >= date.today():

            while ((check_end-check_start).days)>=7:
                check_start = check_start + timedelta(days=1)
            else:
                timeframe = str(check_start) + 'T00 ' + str(check_end) + 'T23'
                return timeframe

        else:
            return timeframe
