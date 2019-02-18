
import matplotlib.pyplot as plt
import numpy as np

def Get_correlation(Trend_data,Stock_data):

    Company = 'AAPL'

    td = Trend_data['Apple Inc.']
    sd = Stock_data['NEON']['close']


    '''
    print(sd)
    print(len(sd))
    print(len(td))
    '''

    # Min-max normalization
    ntd = (td - min(td))/(max(td)-min(td))
    nsd = (sd - min(sd))/(max(sd)-min(sd))
    print(Trend_data['Date'])


    # Create figure and plot both normalized data-set in the same graph.
    plt.plot(ntd,label='Trend Data')
    plt.plot(nsd,label='Stock Data')
    plt.title("Data Correlation")
    plt.legend()
    plt.show()
