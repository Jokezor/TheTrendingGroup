import datetime
import numpy as np
import pandas as pd
import os


def Store(fname,dict):

    f = open(fname,"w")

    i = len(dict["Trend"])

    for j in range(0,i):
        f.write('%s#%s\n' %\
        (dict["Date"][j],dict["Trend"][j]))

    f.close()

    return 0


def Create(fname):

    f  = open(fname,"r")

    if os.stat(fname).st_size == 0:
        return 0

    for i, l in enumerate(f):
        pass

    f.seek(0)

    Element_array = np.empty(i+1, dtype=int)
    Date_array = np.empty(i+1, dtype="datetime64[ns]")
    dict = {'Trend':Element_array,'Date':Date_array}

    j = 0
    for line in f:
        Date, Element = line.strip().split('#',1)
        dict["Date"][j] = Date
        dict["Trend"][j] = Element
        j += 1

    f.close()

    return dict
