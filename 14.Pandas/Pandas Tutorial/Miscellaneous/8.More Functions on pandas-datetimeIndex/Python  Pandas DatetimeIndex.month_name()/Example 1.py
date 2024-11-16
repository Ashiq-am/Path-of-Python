# importing pandas as pd
import pandas as pd

# Create the DatetimeIndex
# Here 'Q' represents quarterly frequency
didx = pd.DatetimeIndex(start ='2018-11-15 09:45:10', freq ='Q', periods = 5)

# Print the DatetimeIndex
print(didx)
