# importing pandas module
import pandas as pd

# reading csv file from url
data = pd.read_csv("https://media.geeksforgeeks.org/wp-content/uploads/nba.csv")

# dropping null value columns to avoid errors
data.dropna(inplace = True)

# creating dictionary for trans table
trans_dict ={"a": "X", "b": "Y", "c": "Z"}

# creating translate table from dictionary
trans_table ="abc".maketrans(trans_dict)

# translating through passed transtable
data["Name"]= data["Name"].str.translate(trans_table)

# display
data
