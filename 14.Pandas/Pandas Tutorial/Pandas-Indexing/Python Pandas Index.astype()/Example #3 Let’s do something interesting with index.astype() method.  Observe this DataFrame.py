# importing pandas module
import pandas as pd

# reading csv file from url
data = pd.read_csv("https://media.geeksforgeeks.org/wp-content/uploads/nba.csv")

# dropping null value columns to avoid errors
data.dropna(inplace=True)

# Setting Number column as index
data = data.set_index('Number')

# Setting index as None
data.index.names = [None]
data.head(5)
