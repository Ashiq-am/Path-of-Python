# importing pandas as pd
import pandas as pd

# list of columns that we want to
# read into the DataFrame
use_cols =['Name', 'Number', 'College']

# Reading the csv file
df = pd.read_csv('nba.csv', usecols = lambda x : x in use_cols,
											index_col = False)

# Print the dataframe
print(df)
