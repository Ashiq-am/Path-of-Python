# importing pandas as pd
import pandas as pd

# Create the PeriodIndex object
pidx = pd.PeriodIndex(start ='2016-02-1 11:32',
		end ='2016-02-01 11:55', freq ='T')

# Print the PeriodIndex object
print(pidx)
