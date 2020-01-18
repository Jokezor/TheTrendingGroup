import os

def Creation(Company, Reset):
    for comp in Company:
        if ((os.path.isfile(comp+"_Bench")==False) or Reset):
            f = open(comp+"_Bench","w+")
            f.write("1970-01-01T00:00:00#0\n") # Store Total Change
            f.write("1970-01-01T00:00:00#0\n") # Store Bench Date
            f.write("1970-01-01T00:00:00#0\n") # Store Current Date
            f.close()

        if ((os.path.isfile(comp+"_Trend")==False) or Reset):
            f  = open(comp+"_Trend","w+")

    return 0
