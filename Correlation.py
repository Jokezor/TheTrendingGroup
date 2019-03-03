'''
    This program is the main file responsible for all the different tests.



    Input: Trend_data (hashtable), Stock_data (hashtable), method (string)
    Output: The analysis which the method (string) specified.

'''
import datetime
from datetime import datetime
from datetime import date, timedelta
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from sklearn import datasets, linear_model
from sklearn.metrics import mean_squared_error, r2_score


def Get_correlation(Trend_data,Stock_data, method, Dates):

    if (method == 'plot'):
        td = Trend_data['Apple Inc.']
        sd = Stock_data['AAPL']['close']

        print "Stock:" + str((len(sd)))
        print "Trend:" + str((len(td)))

        #print (Trend_data['Date'][0]-Dates[0])
        #print ((Trend_data['Date'][0]))
        td_dates = ((Trend_data['Date']).to_pydatetime())


        #td_dates = str(td_dates)
        #td_dates = datetime.datetime.strptime(td_dates, '%Y-%m-%d %H:%M:%S').date()

        #print (td_dates)
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
        td = np.resize(Trend_data['Apple Inc.'],(len(Trend_data['Apple Inc.']),1))
        sd = np.resize(Stock_data['AAPL']['close'],(len(Stock_data['AAPL']['close']),1))

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
