# importing pandas as pd
import pandas as pd

# Creating Timestamp
ts = pd.Timestamp('2019-4-23 11:15:00')

# Create an offset
cbd = pd.tseries.offsets.CustomBusinessDay(n = 3, weekmask = 'Mon Tue Wed Thu')

# Print the Timestamp
print(ts)

# Print the Offset
print(cbd)
