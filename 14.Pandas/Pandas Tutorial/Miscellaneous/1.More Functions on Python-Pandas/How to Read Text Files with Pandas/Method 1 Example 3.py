# Read Text Files with Pandas using read_csv()

# importing pandas
import pandas as pd

# read text file into pandas DataFrame and create
# header with names
df = pd.read_csv("gfg.txt", sep=" ", header=None,
				names=["Team1", "Team2"])

# display DataFrame
print(df)
