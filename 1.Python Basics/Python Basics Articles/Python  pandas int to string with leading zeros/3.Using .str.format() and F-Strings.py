import pandas as pd
# Create a Pandas Series with given values
GFG = pd.Series([7, 25, 326, 38, 5])
# Use .str.format() with
#F-strings to add leading zeros
GFG = GFG.apply(lambda x: f"{x:05}")
# Print the modified Series
print(GFG)
