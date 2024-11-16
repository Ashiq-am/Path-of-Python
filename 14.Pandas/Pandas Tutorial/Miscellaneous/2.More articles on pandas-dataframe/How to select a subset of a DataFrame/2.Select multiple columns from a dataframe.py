# import required module
import pandas as pd

# assign dataframe
data = pd.read_csv("nba.csv")

# get a single columns
name_sex = data[["Name","Age"]]

# dispay the column
name_sex.head()
