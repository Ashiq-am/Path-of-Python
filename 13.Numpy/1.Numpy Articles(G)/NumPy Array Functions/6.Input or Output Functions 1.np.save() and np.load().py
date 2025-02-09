import numpy as np
np.save('array.npy', array)
loaded_array = np.load('array.npy')
print(loaded_array)