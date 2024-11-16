# importing pandas as pd
import pandas as pd

# Creating the dataframe
df = pd.read_csv("nba.csv")

# STD over the column axis.
df.std(axis = 1, skipna = True)
