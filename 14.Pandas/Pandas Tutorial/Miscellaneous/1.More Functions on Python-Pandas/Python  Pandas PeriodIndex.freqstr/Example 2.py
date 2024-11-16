# importing pandas as pd
import pandas as pd

# Create the PeriodIndex object
pidx = pd.PeriodIndex(start ='2011-02-1 ',
			end ='2011-08-14', freq ='M')

# Print the PeriodIndex object
print(pidx)
