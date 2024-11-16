import numpy as np

# Configure NumPy to treat warnings as exceptions
np.seterr(all='raise')
# This will raise exceptions for all warnings
try:
	# Code that might trigger a NumPy warning
	# For example, performing an invalid operation
	result = np.array([0, 1]) / 0
except Warning as e:
	print(f"Caught a NumPy warning: {e}")
except Exception as e:
	print(f"Caught an exception: {e}")
