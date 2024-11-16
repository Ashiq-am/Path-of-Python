''''''
'''In the following example, all the null values in College column has been replaced with “No college” 
string. Firstly, the data frame is imported from CSV and then College column is selected and fillna() 
method is used on it.'''


# importing pandas module
import pandas as pd

# making data frame from csv file
nba = pd.read_csv("nba.csv")

# replacing na values in college with No college
nba["College"].fillna("No College", inplace = True)

nba
