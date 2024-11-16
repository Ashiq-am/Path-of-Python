# importing pandas as pd
import pandas as pd

# Create the TimedeltaIndex object
tidx = pd.TimedeltaIndex(data =['1 days 02:04:00', '1 days 02:03:00',
							'1 days 02:02:00', '1 days 02:01:00'])

# Print the TimedeltaIndex
print(tidx)
