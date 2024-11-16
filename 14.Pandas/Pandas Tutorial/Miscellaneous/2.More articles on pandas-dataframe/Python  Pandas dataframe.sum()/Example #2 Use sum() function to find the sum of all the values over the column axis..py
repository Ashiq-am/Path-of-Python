# importing pandas as pd
import pandas as pd

# Creating the dataframe
df = pd.read_csv("nba.csv")

# sum over the column axis.
df.sum(axis = 1, skipna = True)
