import numpy as np

# Number of weekdays in August 2020
print("Number of saturday in november 2020:",
	np.busday_count('2020-11', '2020-12',
					weekmask='Sat'))
