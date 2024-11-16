import numpy as np

ex4 = np.array([[0.35834379, 0.67202438, np.nan, np.nan,
				np.nan, 0.47870971],
				[np.nan, np.nan, np.nan, 0.08113384,
				0.70511741, 0.15260996],
				[0.09028477, np.nan, 0.16639899,
					0.47740582, 0.7259116, 0.94797347],
				[0.80305651,	 np.nan, 0.67949724,
					0.84112054, 0.15951702, 0.07510587],
				[0.28643337, 0.00804256, 0.36775056,
				0.19360266, 0.07288145, 0.37076932]])

def approach_3(data):
	return data.size - np.count_nonzero(np.isnan(data))

print(approach_3(ex4))
