# importing pandas as pd
import pandas as pd

# Create the PeriodIndex object
pidx = pd.PeriodIndex(start ='2016-8-12 11:12:02',
			end ='2016-08-12 11:32:12', freq ='T')

# Print the PeriodIndex object
print(pidx)
