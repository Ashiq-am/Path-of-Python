# importing pandas as pd
import pandas as pd

# Create the Period object
prd = pd.Period(freq ='T', year = 2006, month = 10,
							hour = 15, minute = 49)

# Print the Period object
print(prd)
