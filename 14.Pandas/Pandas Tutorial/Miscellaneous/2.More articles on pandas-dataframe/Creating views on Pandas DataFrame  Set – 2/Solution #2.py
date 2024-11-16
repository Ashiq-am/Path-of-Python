# importing pandas as pd
import pandas as pd

# list of columns that we do not want
# to read into the DataFrame
skip_cols =['Name', 'Number', 'College']

# Reading the csv file
df = pd.read_csv('nba.csv', usecols = lambda x : x not in skip_cols,
												index_col = False)

# Print the dataframe
print(df)
