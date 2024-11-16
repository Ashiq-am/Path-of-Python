# importing pandas as pd
import pandas as pd

# Creating the dataframe
df = pd.read_csv("nba.csv")

# select all columns except float based
df.select_dtypes(exclude ='float64')
