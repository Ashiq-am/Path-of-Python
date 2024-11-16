# importing pandas as pd
import pandas as pd

# Create the TimedeltaIndex object
tidx = pd.TimedeltaIndex(start ='11 days 22:14:12.001124',
			periods = 5, freq ='T', name ='New_object')

# Print the TimedeltaIndex object
print(tidx)
