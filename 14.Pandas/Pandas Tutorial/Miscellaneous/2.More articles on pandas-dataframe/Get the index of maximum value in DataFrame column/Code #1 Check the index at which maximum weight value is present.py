# importing pandas module
import pandas as pd

# making data frame
df = pd.read_csv("nba.csv")

# Returns index of maximum weight
df[['Weight']].idxmax()
