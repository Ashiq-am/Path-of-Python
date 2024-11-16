# importing pandas as pd
import pandas as pd

# Creating Timestamp
ts = pd.Timestamp('2019-10-10 07:15:11')

# Create the DateOffset
# Also normalize it
do = pd.tseries.offsets.DateOffset(days = 10, hours = 2, normalize = True)

# Print the Timestamp
print(ts)

# Print the DateOffset
print(do)
