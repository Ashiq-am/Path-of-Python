import numpy as np

def log_example2(arr):
	result = np.log(arr)
	return result

# Triggering the warning
result = log_example2(np.array([1, 0, -1]))
print(result)
