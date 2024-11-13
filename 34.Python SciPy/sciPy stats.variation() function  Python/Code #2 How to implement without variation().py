import numpy as np

arr = np.random.randn(5, 5)

print ("array : \n", arr)

# this function works similar to variation()
cv = lambda x: np.std(x) / np.mean(x)

var1 = np.apply_along_axis(cv, axis = 0, arr = arr)
print ("\nVariation at axis = 0: \n", var1)

var2 = np.apply_along_axis(cv, axis = 1, arr = arr)
print ("\nVariation at axis = 0: \n", var2)
