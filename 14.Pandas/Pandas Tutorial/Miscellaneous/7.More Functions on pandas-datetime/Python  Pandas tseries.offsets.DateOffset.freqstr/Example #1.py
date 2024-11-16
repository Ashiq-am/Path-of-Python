# importing pandas as pd
import pandas as pd

# Creating Timestamp
ts = pd.Timestamp('2019-10-10 07:15:11')

# Create the DateOffset
do = pd.tseries.offsets.DateOffset(n = 2)

# Print the Timestamp
print(ts)

# Print the DateOffset
print(do)
