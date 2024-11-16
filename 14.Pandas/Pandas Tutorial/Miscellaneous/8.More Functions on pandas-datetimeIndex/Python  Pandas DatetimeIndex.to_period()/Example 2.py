# importing pandas as pd
import pandas as pd

# Create the DatetimeIndex
# Here 'T' represents minutely frequency
didx = pd.DatetimeIndex(start ='2015-03-02 01:15:12', freq ='T', periods = 5)

# Print the DatetimeIndex
print(didx)
