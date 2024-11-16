# import necessary packages
import numpy as np
from sklearn import preprocessing as p

# create an array
data = np.array([[10, 20], [30, 40],
				[5, 15], [0, 10]])

min_max_scaler = p.MinMaxScaler()
normalizedData = min_max_scaler.fit_transform(data)

# normalized data using MinMaxScaler
print(normalizedData)
