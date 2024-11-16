# importing pandas as pd
import pandas as pd

# Create the PeriodIndex object
pidx = pd.PeriodIndex(start ='2016-8-12 11:32',
			end ='2017-04-05 11:55', freq ='M')

# Print the PeriodIndex object
print(pidx)
