# importing pandas as pd
import pandas as pd

# Create the TimedeltaIndex object
tidx = pd.TimedeltaIndex(data =['1 days 02:00:00', '1 days 06:05:01.000030'])

# Print the TimedeltaIndex
print(tidx)

# Create a copy
tidx_copy = tidx
