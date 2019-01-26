'''
    This program is solely responsable for taking the google trends data and output
    a list with the time and trending data.
    We use a module named pytrends. I can only get it for python 2.7.

    Input: Company and timeframe
    Output: List with the time and corresponding trend data
'''

# To install pytrends:
'''
    1. pip install pytrends
    2. pip install --upgrade --user git+https://github.com/GeneralMills/pytrends
'''
# Python 2.7
# To see documentation and examples follow the link below
# https://github.com/GeneralMills/pytrends

import sys
from pytrends.request import TrendReq

def main():

    Company = sys.argv[1] # Argument 1 since first argument is the program itself
    timefr = sys.argv[2] # Timeframe

    print sys.argv[1]
    print sys.argv[2]

    # Login to Google. Only need to run this once, the rest of requests will use the same session.
    # hl specifies language english and tz specifies Sweden's timezone
    pytrend = TrendReq(hl='en-US', tz=-60)

    # Create payload and capture API tokens. Only needed for interest_over_time(), interest_by_region() & related_queries()
    pytrend.build_payload(kw_list=[Company],timeframe=timefr)

    # Interest Over Time
    interest_over_time_df = pytrend.interest_over_time()
    print(interest_over_time_df)
    return (interest_over_time_df)

main()
