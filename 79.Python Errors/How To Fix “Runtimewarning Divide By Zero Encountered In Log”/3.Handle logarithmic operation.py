import numpy as np

def log_example_fixed(arr):
	# Ignore the warning for invalid logarithmic operations
	with np.errstate(divide='ignore', invalid='ignore'):
		result = np.log(arr)
	return result

# Usage without triggering the warning
result = log_example_fixed(np.array([1, 0, -1]))
print(result)
