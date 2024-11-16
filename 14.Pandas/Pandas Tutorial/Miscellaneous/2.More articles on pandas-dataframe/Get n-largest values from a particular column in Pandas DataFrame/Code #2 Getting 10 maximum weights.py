# importing pandas module
import pandas as pd

# making data frame
df = pd.read_csv("nba.csv")

# Ten largest values in column Weight
df.nlargest(10, ['Weight'])
