# importing pandas as pd
import pandas as pd

# Create the Period object
prd = pd.Period(freq ='S', year = 2006, month = 10,
			hour = 15, minute = 49, second = 17)

# Print the object
print(prd)
