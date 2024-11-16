# importing pandas as pd
import pandas as pd

# Creating Timestamp
ts = pd.Timestamp('2019-10-10 07:15:11')

# Create an offset of 5 Business days
bd = pd.tseries.offsets.BusinessDay(n = 5)

# Print the Timestamp
print(ts)

# Print the DateOffset
print(bd)
