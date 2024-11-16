# importing pandas module
import pandas as pd

# making data frame
df = pd.read_csv("https://media.geeksforgeeks.org/wp-content/uploads/nba.csv")

df1 = df[df['Team'].str.contains('Boston') & df['Position'].str.contains('PG')]
df1
