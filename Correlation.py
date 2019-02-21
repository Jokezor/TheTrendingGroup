'''
    This program is the main file responsible for all the different tests.



    Input: Trend_data (hashtable), Stock_data (hashtable), method (string)
    Output: The analysis which the method (string) specified.

'''

import matplotlib.pyplot as plt
import numpy as np

def Get_correlation(Trend_data,Stock_data, method):

    if (method == 'plot'):
        td = Trend_data['Apple Inc.']
        sd = Stock_data['AAPL']['close']

        # Min-max normalization
        ntd = (td - min(td))/(max(td)-min(td))
        nsd = (sd - min(sd))/(max(sd)-min(sd))

        # Create figure and plot both normalized data-set in the same graph.
        plt.plot(ntd,label='Trend Data')
        plt.plot(nsd,label='Stock Data')
        plt.title("Data Correlation")
        plt.legend()
        plt.show()
        return (0)
    else:
        print("Unknown method: " + str(method))
        return (1)
