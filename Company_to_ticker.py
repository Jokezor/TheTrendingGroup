'''
    The program converts company names (string) to their corresponding ticker
    names (string).

    Input: List of string with company names
    Ouput: List of string with ticker names
'''
import pandas as pd

def Company_to_ticker(Company):

    df = pd.read_csv('secwiki_tickers.csv')
    #dp = pd.read_csv('portfolio.lst',names=['pTicker'])

    #pTickers = dp.pTicker.values  # converts into a list
    #print(type(df))
    tmpTickers = []

    for i in range(len(Company)):
        test = df[df.Name==Company[i]]

        if not (test.empty):
            print test.Ticker.values
    #print(test)


Company = ["Apple Inc."]
Company_to_ticker(Company)

# How to solve synonyms?? (We can manage input so that it matches exactly.)
