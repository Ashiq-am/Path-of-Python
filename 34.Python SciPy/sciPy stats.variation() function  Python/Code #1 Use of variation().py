from scipy.stats import variation
import numpy as np

arr = np.random.randn(5, 5)

print ("array : \n", arr)

# rows: axis = 0, cols: axis = 1

print ("\nVariation at axis = 0: \n", variation(arr, axis = 0))

print ("\nVariation at axis = 1: \n", variation(arr, axis = 1))
