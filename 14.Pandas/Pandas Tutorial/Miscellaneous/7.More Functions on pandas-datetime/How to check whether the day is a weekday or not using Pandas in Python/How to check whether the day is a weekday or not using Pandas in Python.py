# importing Pandas module
import pandas as pd


# Creating a Function
def check_weekday(date):
    # computing the parameter date
    # with len function
    res = len(pd.bdate_range(date, date))

    if res == 0:
        print("This is weekend")
    else:
        print("This is your working day")

    # user input


date = "2020-08-17"
check_weekday(date)

date = "2020-08-16"
check_weekday(date)
