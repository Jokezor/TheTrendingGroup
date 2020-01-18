import os


def Num(Trend_data, Company, percent_change, period_of_change):

    #in_file = open("test.txt", "r+")
    #permchangeoriginalbench = -30   # Those three values will be scanned in or set to standardized values,
    #permchangebench = -30           # probably about 30%, could also use the same scanned value for all 3.
    #permchangeptop = -30
    #percent_change = 0
    lines = []
    lines1 = []
    with open (Company+"_Bench", 'rt') as in_file: # Opening file with current values.
        for line in in_file:
            lines.append(line)

    benchoriginal = float(lines[0][30:33])   # Setting variables for the needed values.
    currentval = float(lines[2][30:32])

    if os.path.isfile('./previousvals.txt'):
        with open ('previousvals.txt', 'rt') as in2_file:  # Opening saved values file for comparison
            for line in in2_file:
                lines1.append(line)
        if ((currentval == lines[1][30:32])):
            updatedbench = currentval / benchoriginal
            print('We have gotten a new benchmark value which is #3.1f of the original benchmark value' % updatedbench)
        pvbenchperiod = float(lines1[0][30:33])  # Setting variables for the needed values.
        pvcurrentval = float(lines1[1][30:32])
        changeptop = currentval - pvcurrentval
        changebenchp = currentval - pvbenchperiod
        #if(user specification)
             # Total change from current benchmark value to current value.
        if (changebenchp > percent_change):
            print('We have an increase in our trend this ' + period_of_change + ' compared to the previous benchmark value of %3.1f percent units.' % changebenchp)
        else:
            print('No increase in our trend this ' + period_of_change + ', decreased by %3.1f percent units compared to the previous benchmark.' % -changebenchp)
        #if(user specification)
                # Total change from past period to this period, either days, weeks, months etc.
        if (changeptop > percent_change):
            print('We have an increase in our trend this ' + period_of_change + ' compared to yesterdays trend of %3.1f. percent units.' % changeptop)
        else:
            print('No increase in our trend this ' + period_of_change + ', decreased by %3.1f percent units compared to last ' % changeptop + period_of_change + '\'s trend.' )

    if not os.path.isfile('./previousvals.txt'):
        benchperiod = float(lines[1][30:33])
        changebenchp = currentval - benchperiod
        if (changebenchp > percent_change):
            print('We have an increase in our trend this ' + period_of_change + ' compared to this periods benchmark value of %3.1f. percent units.' % changebenchp)
        else:
            print('No increase in our trend this ' + period_of_change + ', decreased by %3.1f percent units compared to this periods benchmark.' % -changebenchp)



    # We have to handle 3 cases, whereas the first is the change from designated period to period.
    # 2nd is current period to benchmark for the specified "period to look".
    # And finally the third is current period to the original benchmark.
    #if(user specification)
    changeoriginalbench = currentval - benchoriginal # Total change from original benchmark value to current value.
    if (changeoriginalbench > percent_change):
        print('We have an increase in our trend this ' + period_of_change + ' compared to the original benchmark value of %3.1f. percent units.' % changeoriginalbench)
    else:
        print('No increase in our trend this ' + period_of_change + ', decreased by %3.1f percent units compared to the original benchmark.' % -changeoriginalbench)


    out_file = open("previousvals.txt", "w+")         # Opening another save file to save the neccessary values for next period.
    out_file.write(lines[1])                # Saving the values.
    out_file.write(lines[2])
    out_file.close()
