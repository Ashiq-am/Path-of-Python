# importing pandas as pd
import pandas as pd

# Create the TimedeltaIndex object
tidx = pd.TimedeltaIndex(data =['-3 days 02:10:00',
								'1 days 06:05:01.000030',
								'1 days 02:00:00'], name ='MyObjejct')

# Print the TimedeltaIndex object
print(tidx)
