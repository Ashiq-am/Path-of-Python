# importing pandas as pd
import pandas as pd

# Create the PeriodIndex object
pidx = pd.PeriodIndex(start ='2004-11-11 02:45:21 ',
				end ='2021-5-21 8:45:29', freq ='Y')

# Print the PeriodIndex object
print(pidx)
