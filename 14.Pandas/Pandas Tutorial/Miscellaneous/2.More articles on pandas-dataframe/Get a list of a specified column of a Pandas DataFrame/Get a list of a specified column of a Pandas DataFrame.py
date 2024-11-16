# importing pandas module
import pandas as pd

# making data frame from csv
data = pd.read_csv("nba.csv")

# calling head() method
df = data.head(5)

# displaying data
df
