# import necessary packages
import numpy as np

# create an array
data = np.array([[10, 20], [30, 40],
				[5, 15], [0, 10]])

normalizedData = data/np.sqrt(np.sum(data**2))

# normalized data using sum of squares
print(normalizedData)
