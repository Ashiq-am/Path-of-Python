import numpy as np
import scipy.ndimage

ndarray = np.array([[[11, 12, 13, 14],
					[21, 22, 23, 24]],
					[[31, 32, 33, 34],
					[41, 42, 43, 44]]])

print(scipy.ndimage.zoom(ndarray, (2, 2, 4)))
