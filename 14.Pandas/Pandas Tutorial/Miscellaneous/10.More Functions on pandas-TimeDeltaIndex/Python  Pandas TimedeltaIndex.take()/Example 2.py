# importing pandas as pd
import pandas as pd

# Create the TimedeltaIndex object
tidx = pd.TimedeltaIndex(start ='1 days 02:00:12.001124',
						periods = 5, freq ='D', name ='Koala')

# Print the TimedeltaIndex object
tidx
