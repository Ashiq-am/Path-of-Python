''''''
'''In the following example, method is set as ffill and hence the value in the same column replaces the 
null value. In this case Georgia State replaced null value in college column of row 4 and 5.
Similarly, bfill, backfill and pad methods can also be used.'''


# importing pandas module
import pandas as pd

# making data frame from csv file
nba = pd.read_csv("nba.csv")

# replacing na values in college with No college
nba["College"].fillna( method ='ffill', inplace = True)

nba
