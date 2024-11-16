# Importing modules
import pandas as pd


# creating function
def Time_series(date, per):
    # computing date range with date
    # and given periods
    date_series = pd.date_range(date, periods=per)

    # creating series for date_range
    Result = pd.Series(date_series)
    print(Result)


# Driver Code
# Date in the YYYY-MM-DD format
date = "2020-03-01"

# Number of times the date is
# needed to be printed
per = 10
Time_series(date, per)
