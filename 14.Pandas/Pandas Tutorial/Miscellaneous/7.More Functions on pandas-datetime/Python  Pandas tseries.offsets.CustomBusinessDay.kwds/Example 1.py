# importing pandas as pd
import pandas as pd

# Creating Timestamp
ts = pd.Timestamp('2019-4-23 11:15:00')

# Create an offset
cbd = pd.tseries.offsets.CustomBusinessDay(weekmask = 'Mon Tue Wed')

# Print the Timestamp
print(ts)

# Print the Offset
print(cbd)
