# importing pandas as pd
import pandas as pd

# Read the data into a series
sr = pd.Series.from_csv('nba.csv', index_col = 1)

# Print the first 10 rows of series
print(sr.head(10))
