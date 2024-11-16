# importing pandas as pd
import pandas as pd

# read the csv file and create DataFrame
df = pd.read_csv('nba.csv')

# reset the index name
df.rename_axis('Index_name', axis = 'rows')

# Print the DataFrame
print(df)
