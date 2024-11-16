# importing pandas module
import pandas as pd

# making data frame
df = pd.read_csv("nba.csv")

df.nsmallest(10, ['Weight'])
