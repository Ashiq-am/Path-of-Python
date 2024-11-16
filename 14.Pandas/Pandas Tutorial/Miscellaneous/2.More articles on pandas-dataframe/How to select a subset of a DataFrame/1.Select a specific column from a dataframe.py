# import required module
import pandas as pd

# assign dataframe
data = pd.read_csv("nba.csv")

# get a single columns
ages = data["Age"]

# dispay the column
ages.head()
