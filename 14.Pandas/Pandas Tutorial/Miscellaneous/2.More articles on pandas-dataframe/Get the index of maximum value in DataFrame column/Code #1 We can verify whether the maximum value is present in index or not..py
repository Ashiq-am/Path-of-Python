# importing pandas module
import pandas as pd

# making data frame
df = pd.read_csv("nba.csv")

# from index 400 to 409
df.iloc[400:410]
