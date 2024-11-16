# importing pandas as pd
import pandas as pd

# Creating the Series
sr = pd.Series([b"b'New_York'", b"b'Lisbon'", b"b'Tokyo'", b"b'Paris'", b"b'Munich'"])

# Creating the index
idx = ['City 1', 'City 2', 'City 3', 'City 4', 'City 5']

# set the index
sr.index = idx

# Print the series
print(sr)
