# importing pandas module
import pandas as pd

# making data frame from csv file
nba = pd.read_csv("nba.csv")

# replacing na values in college with No college
nba["College"].fillna( method ='ffill', limit = 1, inplace = True)

nba
