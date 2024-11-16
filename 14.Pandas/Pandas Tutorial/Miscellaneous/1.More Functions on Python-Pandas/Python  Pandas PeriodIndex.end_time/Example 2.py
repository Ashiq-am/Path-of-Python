# importing pandas as pd
import pandas as pd

# Create the PeriodIndex object
pidx = pd.PeriodIndex(start ='2011-02-14 04:30',
			end ='2011-02-14 11:44', freq ='H')

# Print the PeriodIndex object
print(pidx)
