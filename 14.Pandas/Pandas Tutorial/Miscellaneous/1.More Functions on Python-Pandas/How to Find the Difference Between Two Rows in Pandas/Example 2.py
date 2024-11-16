# Importing Pandas Library
import pandas as pd

# Creating dummy DataFrame for testing
df = pd.DataFrame({ 'a': [1, 2, 3, 4, 5, 6],
					'b': [8, 18, 27, 20, 33, 49],
					'c': [2, 24, 6, 16, 20, 52]})
# Printing DataFrame before applying diff function
print(df)

# Printing DataFrame after applying diff function
print("Difference: ")
print(df.diff(periods=2))
