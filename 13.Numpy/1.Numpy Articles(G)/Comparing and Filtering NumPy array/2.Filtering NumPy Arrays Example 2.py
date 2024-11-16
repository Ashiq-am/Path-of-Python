# Importing NumPy Module
import numpy as np

# Creating Array
a = np.array([1, 2, 3, 40, 50, 100,
			45, 87, 98])

# Filtering Condition
filter2 = a % 2 == 0
even = np.array([filter2])
print(*even)
