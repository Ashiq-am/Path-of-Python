import pandas as pd

# Create a Series with nullable integers
s = pd.Series([1, 2, None], dtype="Int64")

# Perform arithmetic operation and comparison
s_plus_one = s + 1  # Adds 1 to each element in the series
comparison = s == 1  # Checks if each element in the series is equal to 1

# Output the results
print(s_plus_one)
print(comparison)
