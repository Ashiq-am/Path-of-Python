# Import pandas package
import pandas as pd

# making data frame
data = pd.read_csv("nba.csv")

row_count = 0

# iterating over indices
for col in data.index:
    row_count += 1

# print the row count
print(row_count)
