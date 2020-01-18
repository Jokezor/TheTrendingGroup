'''
    The program converts company names (string) to their corresponding ticker
    names (string).

    Input: List of string with company names
    Ouput: List of string with ticker names, Hashtable with holiday dates for
           each year, Each year's holidays in a list in 'Month-Day' format.
'''
import pandas as pd

def Company_to_ticker(Company):

    # Nasdaq
    df = pd.read_csv('Nasdaq/companylist.csv')

    tmpTickers = []
    for i in range(len(Company)):
        test = df[df.Name==Company[i]]

        if not (test.empty):
            tmpTickers.append(test.Symbol.values[0])

    # Return the tickers if the Company was listed in Nasdaq
    if  len(tmpTickers)!=0:
        Closed_days = {}
        # Need to return also a list of all the nasdaq holidays
        # Need to check if these get updated during the year..
        # 'Month-Day'
        Closed_days['2015'] = ['01-01','01-19','02-16','04-03','05-25','07-03','09-07','11-26','12-25']
        Closed_days['2016'] = ['01-01','01-18','02-15','03-25','05-30','07-04','09-05','11-24','12-26']
        Closed_days['2017'] = ['01-02','01-16','02-20','04-14','05-29','07-04','09-04','11-23','12-25']
        Closed_days['2018'] = ['01-01','01-15','02-19','03-30','05-28','07-04','09-03','11-22','12-05','12-25']
        Closed_days['2019'] = ['01-01','01-21','02-18','04-19','05-27','07-04','09-02','11-28','12-25']
        Closed_days['2020'] = ['01-01','01-20','02-17','04-10','05-25','07-03','09-07','11-26','12-25']
        Closed_days['2021'] = ['01-01','01-18','02-15','04-02','05-31','07-05','09-06','11-25','12-24']

        return tmpTickers, Closed_days

    # New York Stock Exchange
    df = pd.read_csv('NYSE/companylist.csv')

    tmpTickers = []
    for i in range(len(Company)):
        test = df[df.Name==Company[i]]

        if not (test.empty):
            tmpTickers.append(test.Symbol.values[0])

    # Return the tickers if the Company was listed in NYSE
    if  len(tmpTickers)!=0:
        Closed_days = {}
        # Need to return also a list of all the nasdaq holidays
        # Need to check if these get updated during the year..
        # 'Month-Day'
        Closed_days['2015'] = ['01-01','01-19','02-16','04-03','05-25','07-03','09-07','11-26','12-25']
        Closed_days['2016'] = ['01-01','01-18','02-15','03-25','05-30','07-04','09-05','11-24','12-26']
        Closed_days['2017'] = ['01-02','01-16','02-20','04-14','05-29','07-04','09-04','11-23','12-25']
        Closed_days['2018'] = ['01-01','01-15','02-19','03-30','05-28','07-04','09-03','11-22','12-05','12-25']
        Closed_days['2019'] = ['01-01','01-21','02-18','04-19','05-27','07-04','09-02','11-28','12-25']
        Closed_days['2020'] = ['01-01','01-20','02-17','04-10','05-25','07-03','09-07','11-26','12-25']
        Closed_days['2021'] = ['01-01','01-18','02-15','04-02','05-31','07-05','09-06','11-25','12-24']

        return tmpTickers, Closed_days
