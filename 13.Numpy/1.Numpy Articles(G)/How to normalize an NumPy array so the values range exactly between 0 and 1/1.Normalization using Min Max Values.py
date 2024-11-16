# import necessary packages
import numpy as np

# create an array
data = np.array([[10, 20], [30, 40],
				[5, 15], [0, 10]])

normalizedData = (data-np.min(data))/(np.max(data)-np.min(data))

# normalized data using min max value
print(normalizedData)
