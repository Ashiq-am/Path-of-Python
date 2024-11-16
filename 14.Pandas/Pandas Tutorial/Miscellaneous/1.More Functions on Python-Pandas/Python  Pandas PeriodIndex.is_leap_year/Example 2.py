# importing pandas as pd
import pandas as pd

# Create the PeriodIndex object
pidx = pd.PeriodIndex(start ='2016-02-1',
		end ='2016-02-06', freq ='D')

# Print the PeriodIndex object
print(pidx)
