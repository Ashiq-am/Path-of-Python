# Import the numpy library
import numpy as np

# Create a numpy array
arr = np.array([1,5,4])

# Divide by zero Exception
with warnings.catch_warnings():
	try:
		answer = arr / 0
	except Warning as e:
		print('error found:', e)
