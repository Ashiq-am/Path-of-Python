# importing pandas as pd
import pandas as pd

# Create the DatetimeIndex
# Here 'D' represents calendar day frequency
didx = pd.DatetimeIndex(start ='2014-08-01 10:05:45', freq ='D', periods = 5)

# Print the DatetimeIndex
print(didx)
