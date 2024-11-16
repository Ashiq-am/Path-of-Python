# importing pandas as pd
import pandas as pd

# Create the Period object
prd = pd.Period(freq ='S', year = 2000, month = 2, day = 22,
						hour = 8, minute = 21, second = 24)

# Print the Period object
print(prd)
