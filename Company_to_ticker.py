'''
    The program converts company names (string) to their corresponding ticker
    names (string).

    Input: List of string with company names
    Ouput: List of string with ticker names
'''
import pandas as pd

def Company_to_ticker(Company):


    # Nasdaq
    df = pd.read_csv('companylist.csv')

    tmpTickers = []
    for i in range(len(Company)):
        test = df[df.Name==Company[i]]

        if not (test.empty):
            tmpTickers.append(test.Symbol.values[0])

    # Return the tickers if the Company was listed in Nasdaq
    if  len(tmpTickers)!=0:
        # Need to return also a list of all the nasdaq holidays
        # 'Month-Day'
        Nasdaq_closed = ['01-01','01-21','02-18','04-19','05-27','07-04','09-02','11-28','12-25']
        return tmpTickers, Nasdaq_closed
