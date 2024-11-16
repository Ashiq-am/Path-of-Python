

# importing pandas as pd
import pandas as pd

# Create the Timestamp object
ts = pd.Timestamp(year = 2009, month = 5, day = 31,
	hour = 4, second = 49, tz = 'Europe/Berlin')

# Print the Timestamp object
print(ts)