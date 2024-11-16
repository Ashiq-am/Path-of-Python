# importing pandas as pd
import pandas as pd

# Create the TimedeltaIndex object
tidx = pd.TimedeltaIndex(start ='1 days 06:05:01.000030',
				periods = 5, freq ='D', name ='Koala')

# Print the TimedeltaIndex object
print(tidx)
