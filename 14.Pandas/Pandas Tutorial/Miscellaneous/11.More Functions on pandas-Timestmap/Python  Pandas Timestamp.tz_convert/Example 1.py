# importing pandas as pd
import pandas as pd

# Create the Timestamp object
ts = pd.Timestamp(year = 2011, month = 11, day = 21,
				hour = 10, second = 49, tz = 'US/Central')

# Print the Timestamp object
print(ts)
