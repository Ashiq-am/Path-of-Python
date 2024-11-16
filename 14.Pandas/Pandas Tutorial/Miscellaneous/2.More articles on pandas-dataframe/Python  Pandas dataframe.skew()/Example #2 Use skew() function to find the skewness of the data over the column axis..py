# importing pandas as pd
import pandas as pd

# Creating the dataframe
df = pd.read_csv("nba.csv")

# skip the na values
# find skewness in each row
df.skew(axis = 1, skipna = True)
