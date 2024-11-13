import pandas as pd
# Create a pandas Series with the given values [7, 15, 346, 68, 8]
D = pd.Series([7, 15, 346, 68, 8])
D = D.map('{:04}'.format)
# Print the formatted Series
print(D)
