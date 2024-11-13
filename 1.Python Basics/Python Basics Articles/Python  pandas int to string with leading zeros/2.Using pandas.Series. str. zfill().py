import pandas as pd
# Create a Pandas Series with
# given values
D = pd.Series([7, 15, 356, 58, 5])
D = D.astype(str).str.zfill(5)
# Print the modified Series
print(D)
