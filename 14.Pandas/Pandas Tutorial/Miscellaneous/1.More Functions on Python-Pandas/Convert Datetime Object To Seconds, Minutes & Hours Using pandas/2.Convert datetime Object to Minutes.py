import pandas as pd

# Create a datetime object
dt = pd.to_datetime('2024-02-07 12:34:56')

minutes = dt.minute
print("Minutes:", minutes)
