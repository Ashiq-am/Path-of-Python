# importing pandas module
import pandas as pd

# making data frame
df = pd.read_csv("https://media.geeksforgeeks.org/wp-content/uploads/nba.csv")

df['Name'].head(10)

# get multiple elements at given index
ser[[0, 3, 6, 9]]
