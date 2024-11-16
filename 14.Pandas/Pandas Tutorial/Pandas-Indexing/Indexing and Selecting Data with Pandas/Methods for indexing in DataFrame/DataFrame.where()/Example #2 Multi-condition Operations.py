# importing pandas package
import pandas as pd

# making data frame from csv file
data = pd.read_csv("nba.csv")

# sorting dataframe
data.sort_values("Team", inplace = True)

# making boolean series for a team name
filter1 = data["Team"]=="Atlanta Hawks"

# making boolean series for age
filter2 = data["Age"]>24

# filtering data on basis of both filters
data.where(filter1 & filter2, inplace = True)

# display
data




"""
Data is filtered on the basis of both Team and Age. 
Only the rows having Team name “Atlanta Hawks” and players having age 
above 24 will be displayed.

"""
