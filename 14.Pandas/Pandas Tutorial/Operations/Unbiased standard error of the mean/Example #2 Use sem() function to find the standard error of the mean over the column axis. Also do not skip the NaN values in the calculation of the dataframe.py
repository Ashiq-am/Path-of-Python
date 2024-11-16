# importing pandas as pd
import pandas as pd

# Creating the dataframe
df = pd.read_csv("nba.csv")

# Calculate the standard error of
# the mean of all the rows in dataframe
df.sem(axis = 1, skipna = False)
