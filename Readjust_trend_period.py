'''
    This script will take in the Trending Data and period_of_change
    and make sure the trending data is average according to the period_of_change.

    Input: Trend_data (Hashtable with Trending factors for each company and
    dates), period_of_change (string)

    Output: Trend_data (Hashtable with Trending factors for each company and
    dates)

'''
import datetime

def Readjust(Trend_data, period_of_change):

    td_dates = ((Trend_data['Date']).to_pydatetime())
    New_Trend_data = {}

    index = 0
    for company in Trend_data:
        index=index+1

        # To skip the last index "company" in Trend_data which is Date.
        if index<len(Trend_data):
            prevday=datetime.datetime.strptime(str(td_dates[0])[0:10], "%Y-%m-%d").date()

            count=0
            sum=0
            Trend = []
            Dates = []

            # If there is one time that is 100, we lose the 100 index. We still get the best day though.
            for i in range(0,len(td_dates)):
                curr_day = datetime.datetime.strptime(str(td_dates[i])[0:10], "%Y-%m-%d").date()
                if curr_day==datetime.datetime.strptime(str(td_dates[(i+1)%len(td_dates)])[0:10], "%Y-%m-%d").date():
                    count=count+1
                    sum = sum + Trend_data[company][i]

                elif count>0:
                    count=count+1
                    sum = sum + Trend_data[company][i]
                    #print Dates
                    Trend.append(sum/count)
                    Dates.append(prevday)

                    count=0
                    sum=0

                prevday=curr_day
            New_Trend_data["Date"] = Dates
            New_Trend_data[company] = Trend


    if len(Dates)>0:
        return New_Trend_data
    else:
        return Trend_data
