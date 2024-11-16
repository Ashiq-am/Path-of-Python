import numpy as np

ex3 = np.array([[3, 4, -390, np.nan],
				[np.nan, np.nan, np.nan, -90]])

def approach_2(data):
	return np.sum(~np.isnan(data))

print(approach_2(ex3))
