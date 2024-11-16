# importing pandas as pd
import pandas as pd

# Create the TimedeltaIndex object
tidx = pd.TimedeltaIndex(data =[None, '1 days 06:05:01.000030', None,
								'1 days 02:00:00', '21 days 06:15:01.000030'],
														name ='Old_object')

# Print the TimedeltaIndex object
print(tidx)
