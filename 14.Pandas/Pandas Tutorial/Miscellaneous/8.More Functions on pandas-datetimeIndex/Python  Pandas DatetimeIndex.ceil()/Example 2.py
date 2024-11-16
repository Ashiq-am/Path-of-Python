# importing pandas as pd
import pandas as pd

# Create the DatetimeIndex
# Here 'T' represents minutely frequency
didx = pd.DatetimeIndex(start ='2018-11-15 09:45', freq ='T', periods = 5)

# Print the DatetimeIndex
print(didx)
