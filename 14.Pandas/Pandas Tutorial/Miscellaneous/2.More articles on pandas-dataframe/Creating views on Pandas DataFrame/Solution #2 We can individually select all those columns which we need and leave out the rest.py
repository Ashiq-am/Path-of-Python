# importing pandas as pd
import pandas as pd

# Reading the csv file
df = pd.read_csv("nba.csv")

# select the first three columns
# and store the result in a new dataframe
df_copy = df.iloc[:, 0:3]

# Print the new DataFrame
df_copy
