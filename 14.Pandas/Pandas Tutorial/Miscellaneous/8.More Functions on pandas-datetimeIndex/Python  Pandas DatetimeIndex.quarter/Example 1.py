# importing pandas as pd
import pandas as pd

# Create the DatetimeIndex
# Here 'M' represents Monthly frequency
didx = pd.DatetimeIndex(start ='2014-08-01 10:05:45', freq ='M',
							periods = 5, tz ='Asia/Calcutta')

# Print the DatetimeIndex
print(didx)
