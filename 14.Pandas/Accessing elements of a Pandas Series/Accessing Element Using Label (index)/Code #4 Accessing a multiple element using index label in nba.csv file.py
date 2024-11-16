# importing pandas module
import pandas as pd

# making data frame
df = pd.read_csv("nba.csv")

ser = pd.Series(df['Name'])
ser.head(10)
