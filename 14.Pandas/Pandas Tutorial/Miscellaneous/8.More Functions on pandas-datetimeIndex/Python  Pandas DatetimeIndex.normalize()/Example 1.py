# importing pandas as pd
import pandas as pd

# Create the DatetimeIndex
# Here 'H' represents hourly frequency
idx = pd.DatetimeIndex(start ='2018-08-10 08:00', freq ='H',
						periods = 5, tz ='Asia/Calcutta')

# Print the DatetimeIndex
print(didx)
