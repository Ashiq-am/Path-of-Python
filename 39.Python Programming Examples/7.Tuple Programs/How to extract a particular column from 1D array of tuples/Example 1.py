import numpy as np

# define a 1d array of tuples
arr = np.array([(18.18, 2.27, 3.23), (36.43, 34.24, 6.6),
				(5.25, 6.16, 7.7), (7.37, 28.8, 8.9)])

# slice the array by passing the
# column number
arr[:, 2]
