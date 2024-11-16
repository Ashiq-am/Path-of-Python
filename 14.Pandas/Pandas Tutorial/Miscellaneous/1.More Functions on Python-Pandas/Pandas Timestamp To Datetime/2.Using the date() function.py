# Sample dataset using dictionaries
data = {
	'timestamp': ['2024-01-01 12:00:00', '2024-01-02 14:30:00', '2024-01-03 08:45:00'],
	'value': [10, 20, 15]
}

import pandas as pd

# Create a Timestamp object
ts = pd.Timestamp("2024-02-05 10:00:00")

# Extract the date using the date() method
date_obj = ts.date()

print(type(ts))
print(type(date_obj))
