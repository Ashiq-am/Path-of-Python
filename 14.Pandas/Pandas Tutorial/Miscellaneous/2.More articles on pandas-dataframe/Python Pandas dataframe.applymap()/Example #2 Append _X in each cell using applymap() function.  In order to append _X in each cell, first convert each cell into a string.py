# importing pandas as pd
import pandas as pd

# Making data frame from the csv file
df = pd.read_csv("nba.csv")

# Using applymap() to append '_X'
# in each cell of the dataframe
df.applymap(lambda x: str(x) + '_X')
