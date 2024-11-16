# importing pandas as pd
import pandas as pd

# Creating the dataframe
df = pd.read_csv("nba.csv")

# Applying get_dtype_counts() function to
# find the data type counts in modified dataframe.
df[["Salary", "Name", "Team"]].get_dtype_counts()
