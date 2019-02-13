'''
    The program converts company names (string) to their corresponding ticker
    names (string).

    Input: List of string with company names
    Ouput: List of string with ticker names
'''
import pandas as pd

def Company_to_ticker(Company):

    df = pd.read_csv('companylist.csv')

    tmpTickers = []

    for i in range(len(Company)):
        test = df[df.Name==Company[i]]

        if not (test.empty):
            tmpTickers.append(test.Symbol.values[0])

    return tmpTickers
