'''
    This program is solely responsable for taking the input from the user and output
    the correct timeframe.

    Input: From the user
    Output: Company, period_to_look, period_of_change, percent_change
'''
import time

def Ask_dates():

    # Welcome message
    print("Welcome to TheTrendingGroup's Trend and Stock Analysis tool. \nInput Company and timeframes to look for increase in trending factor to get analysis.\n")

    time.sleep(2)

    Company = input("What Company/Companies do you want to look at? \n")

    # Placeholder name
    period_to_look = "Decade"

    # Currently only works for year, month and week
    while(period_to_look != "Year" and period_to_look != "Month" and period_to_look != "Week" and period_to_look != "Day"):
        period_to_look = input("\nWhat period are you interested in as a benchmark? \n(Year, Month, Week, Day)\n")

        # Keep asking the user to specify correct
        if((period_to_look != "Year" and period_to_look != "Month" and period_to_look != "Week" and period_to_look != "Day")):
            print ("\n" + "Wrong Input: " + period_to_look + "\n" +  "Try Again.")

    # Placeholder name
    period_of_change = "Decade"

    # Currently only works for monthly, weekly and dayly
    while(period_of_change != "Month" and period_of_change != "Week" and period_of_change != "Day"):

        if (period_to_look == "Year"):
            period_of_change = input("\nWhat period are you interested to check increase? \n(Month,Week,Day)\n")
            # Keep asking the user to specify correct
            if((period_of_change != "Month" and period_of_change != "Week" and period_of_change != "Day")):
                print ("\n" + "Wrong Input: " + period_of_change + "\n" +  "Try Again.")
                period_of_change = 0

        if (period_to_look == "Month"):
            period_of_change = input("\nWhat period are you interested to check increase? \n(Month,Week,Day)\n")
            # Keep asking the user to specify correct
            if((period_of_change != "Month" and period_of_change != "Week" and period_of_change != "Day")):
                print ("\n" + "Wrong Input: " + period_of_change + "\n" +  "Try Again.")
                period_of_change = 0

        if (period_to_look == "Week"):
            period_of_change = input("\nWhat period are you interested to check increase? \n(Week,Day)\n")
            # Keep asking the user to specify correct
            if((period_of_change != "Week" and period_of_change != "Day")):
                print ("\n" + "Wrong Input: " + period_of_change + "\n" +  "Try Again.")
                period_of_change = 0

        if (period_to_look == "Day"):
            period_of_change = input("\nWhat period are you interested to check increase? \n(Day)\n")
            # Keep asking the user to specify correct
            if((period_of_change != "Day")):
                print ("\n" + "Wrong Input: " + period_of_change + "\n" +  "Try Again.")
                period_of_change = 0


    # Placeholder value
    percent_change = 0
    while((percent_change <= 0) or (percent_change > 100)):

        # Get the percentage change
        percent_change = int(input("\nHow much percentage change for notification? \n(1-100\%)\n"))

        # Keep asking the user to specify correct
        if((percent_change <= 0) or (percent_change > 100)):
            print ("\n" + "Wrong Input: " + str(percent_change) + "\n" +  "Try Again.")


    return [Company], period_to_look, period_of_change, percent_change
