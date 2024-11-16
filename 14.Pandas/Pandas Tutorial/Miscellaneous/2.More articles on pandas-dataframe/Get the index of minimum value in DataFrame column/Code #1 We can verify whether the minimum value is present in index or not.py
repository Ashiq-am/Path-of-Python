
# importing pandas module
import pandas as pd

# making data frame
df = pd.read_csv("nba.csv")

# from index 140 to 154
df.iloc[140:155]
