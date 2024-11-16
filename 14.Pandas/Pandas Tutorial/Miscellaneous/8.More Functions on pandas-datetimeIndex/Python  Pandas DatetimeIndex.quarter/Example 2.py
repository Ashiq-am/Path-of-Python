# importing pandas as pd
import pandas as pd

# Create the DatetimeIndex
# Here 'Q' represents Quarterly frequency
didx = pd.DatetimeIndex(start ='2000-01-10 06:30', freq ='Q',
						periods = 5, tz ='Asia/Calcutta')

# Print the DatetimeIndex
print(didx)
