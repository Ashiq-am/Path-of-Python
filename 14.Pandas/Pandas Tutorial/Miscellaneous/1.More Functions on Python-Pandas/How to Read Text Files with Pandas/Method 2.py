# Read Text Files with Pandas using read_table()

# importing pandas
import pandas as pd

# read text file into pandas DataFrame
df = pd.read_table("gfg.txt", delimiter=" ")

# display DataFrame
print(df)
