# importing pandas as pd
import pandas as pd

# Making data frame from the csv file
df = pd.read_csv("nba.csv")

# Drop the rows with 'nan' values
df = df.dropna()

# print the existing data type of each column
df.info()
