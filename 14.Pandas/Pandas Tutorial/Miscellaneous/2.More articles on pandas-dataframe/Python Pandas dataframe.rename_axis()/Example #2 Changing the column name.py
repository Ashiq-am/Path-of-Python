# importing pandas as pd
import pandas as pd

# Making data frame from the csv file
df = pd.read_csv("nba.csv")

# this will add '_X' at the end of each column name
df.rename_axis(lambda x:x+"_X", axis ="columns")
