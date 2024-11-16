# import library
import numpy as np

# create a 1d-array
ini_array = np.array([10, 20, 5,
					10, 8, 20,
					8, 9])

# Get a tuple of unique values
# and their frequency in
# numpy array
unique, frequency = np.unique(ini_array,
							return_counts = True)

# convert both into one numpy array
# and then transpose it
count = np.asarray((unique,frequency )).T

print("The values and their frequency are in transpose form:\n",
	count)
