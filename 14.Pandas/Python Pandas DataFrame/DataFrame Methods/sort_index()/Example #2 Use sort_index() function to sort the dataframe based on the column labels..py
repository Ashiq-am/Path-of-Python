# importing pandas as pd
import pandas as pd

# Creating the dataframe
df = pd.read_csv("nba.csv")

# sorting based on column labels
df.sort_index(axis = 1)
