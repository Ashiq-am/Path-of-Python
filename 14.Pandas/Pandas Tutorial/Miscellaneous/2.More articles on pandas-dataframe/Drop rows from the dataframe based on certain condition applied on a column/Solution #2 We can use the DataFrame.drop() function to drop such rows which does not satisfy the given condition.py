# importing pandas as pd
import pandas as pd

# Read the csv file and construct the
# dataframe
df = pd.read_csv('nba.csv')

# First filter out those rows which
# does not contain any data
df = df.dropna(how = 'all')

# Filter all rows for which the player's
# age is greater than or equal to 25
df.drop(df[df['Age'] < 25].index, inplace = True)

# Print the modified dataframe
print(df.head(15))

# Print the shape of the dataframe
print(df.shape)
