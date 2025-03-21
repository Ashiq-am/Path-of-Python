'''
 In this example, rows having particular Team name will be shown and
 rest will be replaced by NaN using .where() method.

'''


# importing pandas package
import pandas as pd

# making data frame from csv file
data = pd.read_csv("nba.csv")

# sorting dataframe
data.sort_values("Team", inplace = True)

# making boolean series for a team name
filter = data["Team"]=="Atlanta Hawks"

# filtering data
data.where(filter, inplace = True)

# display
data
