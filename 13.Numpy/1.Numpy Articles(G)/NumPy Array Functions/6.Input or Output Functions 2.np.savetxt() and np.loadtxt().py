import numpy as np
np.savetxt('array.txt', array)
loaded_array = np.loadtxt('array.txt')
print(loaded_array)