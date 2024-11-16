import pandas as pd

data = [1, 1, 0, 1, 0, 1, 1, 0, 0, 1, 1, 1]

# Create Data Frame using pandas library
# .value_counts() counts the number of
# occurrences of particular observation

df = pd.Series(data).value_counts()
print(df)
