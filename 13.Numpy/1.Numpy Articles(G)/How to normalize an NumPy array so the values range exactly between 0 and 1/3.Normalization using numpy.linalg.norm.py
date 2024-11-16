# import necessary packages
import numpy as np

# create an array
data = np.array([[10, 20], [30, 40],
				[5, 15], [0, 10]])

normalizedData = data/np.linalg.norm(data)

# normalized data using linalg.norm
print(normalizedData)
