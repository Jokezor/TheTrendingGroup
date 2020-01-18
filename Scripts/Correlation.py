'''
    This program is the main file responsible for all the different tests.


    Input: Trend_data (hashtable), Stock_data (hashtable), method (string)
    Output: The analysis which the method (string) specified.

'''
#import datetime
#from datetime import datetime
#from datetime import date, timedelta
import matplotlib.pyplot as plt
import numpy as np
from sklearn import datasets, linear_model
from sklearn.metrics import mean_squared_error, r2_score

def Get_correlation(Trend_data,Stock_data, method):

    # Get all data
    td = Trend_data['Tesla, Inc. ']

    if str(type(Trend_data['Date'])) == '<type \'list\'>':
        td_dates = ((Trend_data['Date']))
    else:
        td_dates = ((Trend_data['Date']).to_pydatetime())


    sd = Stock_data['TSLA']['close']

    #print (td_dates)
    #print Stock_data['TSLA']['Date']


    # If not the same amount of data
    if (len(sd)) != (len(td)):
        print "\n \nERROR MESSAGE: Different length of trending data and stock data! \n"
        print "Stock length:" + str((len(sd)))
        print "Trend length:" + str((len(td)))
        return 1

    if (method == 'plot'):

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
    elif (method == 'Linear Regression'):
        # Load the diabetes dataset
        diabetes = datasets.load_diabetes()
        td = np.resize(Trend_data['Tesla, Inc. '],(len(Trend_data['Tesla, Inc. ']),1))
        sd = np.resize(Stock_data['TSLA']['close'],(len(Stock_data['TSLA']['close']),1))

        #print(td.shape)
        #print(sd.shape)
        #print()
        # Use only one feature
        #diabetes_X = diabetes.data[:, np.newaxis, 2]

        # Split the data into training/testing sets
        #diabetes_X_train = diabetes_X[:-20]
        #diabetes_X_test = diabetes_X[-20:]
        Trend_train = td[:-20]
        Trend_test = td[-20:]

        Stock_train = sd[:-20]
        Stock_test = sd[-20:]


        #print((diabetes_X).shape)

        # Split the targets into training/testing sets
        #diabetes_y_train = diabetes.target[:-20]
        #diabetes_y_test = diabetes.target[-20:]

        # Create linear regression object
        regr = linear_model.LinearRegression()

        regr.fit(Trend_train,Stock_train)
        #Trend_train.reshape(-1,1)
        # Train the model using the training sets
        #regr.fit(Trend_train, Stock_train)

        # Make predictions using the testing set
        Stock_pred = regr.predict(Trend_test)

        # The coefficients
        print('Coefficients: \n', regr.coef_)
        # The mean squared error
        print("Mean squared error: %.2f"
              % mean_squared_error(Stock_test, Stock_pred))
        # Explained variance score: 1 is perfect prediction
        print('Variance score: %.2f' % r2_score(Stock_test, Stock_pred))

        # Plot outputs
        plt.scatter(Trend_test, Stock_test,  color='black')
        plt.plot(Trend_test, Stock_pred, color='blue', linewidth=3)

        plt.xticks(())
        plt.yticks(())

        plt.show()

    else:
        print("Unknown method: " + str(method))
        return (1)
