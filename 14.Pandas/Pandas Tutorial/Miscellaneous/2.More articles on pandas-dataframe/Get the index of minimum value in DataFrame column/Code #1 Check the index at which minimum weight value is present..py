# importing pandas module
import pandas as pd

# making data frame
df = pd.read_csv("nba.csv")

# Returns index of minimum weight
df[['Weight']].idxmin()
