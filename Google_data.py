'''
    This program is solely responsable for taking the google trends data and output
    a list with the time and trending data.
    We use a module named pytrends. I can only get it for python 2.7.

    Input: Company and timeframe
    Output: Hashtable with the time and corresponding trend data
'''

# To install pytrends:
'''
    1. pip install pytrends
    2. pip install --upgrade --user git+https://github.com/GeneralMills/pytrends
'''
# Python 2.7
# To see documentation and examples follow the link below
# https://github.com/GeneralMills/pytrends

# I did some work here, shouldn't affect the master.

from pytrends.request import TrendReq

def Trending_google(Company,timefr):

    # Create hashtable to store time and corresponding trend data
    Trend_data = {}

    # Login to Google. Only need to run this once, the rest of requests will use the same session.
    # hl specifies language english and tz specifies Sweden's timezone
    pytrend = TrendReq(hl='en-US', tz=-60)

    # Create payload and capture API tokens. Only needed for interest_over_time(), interest_by_region() & related_queries()
    pytrend.build_payload(kw_list=[Company],timeframe=timefr)

    # Interest Over Time from google trends
    interest_over_time_df = pytrend.interest_over_time()

    # Store the data in the hashtable
    Trend_data["Trend"] = interest_over_time_df.values[:,0]
    Trend_data["Date"] = interest_over_time_df.index

    return (Trend_data)
