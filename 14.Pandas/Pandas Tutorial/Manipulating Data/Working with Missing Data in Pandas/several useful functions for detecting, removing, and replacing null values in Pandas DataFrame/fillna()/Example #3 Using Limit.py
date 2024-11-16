''''''
'''In this example, a limit of 1 is set in the fillna() method to check if the function stops 
replacing after one successful replacement of NaN value or not.'''


# importing pandas module
import pandas as pd

# making data frame from csv file
nba = pd.read_csv("nba.csv")

# replacing na values in college with No college
nba["College"].fillna( method ='ffill', limit = 1, inplace = True)

nba
