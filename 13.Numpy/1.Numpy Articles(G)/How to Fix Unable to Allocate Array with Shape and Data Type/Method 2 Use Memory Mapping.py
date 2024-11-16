import numpy as np
arr = np.memmap('large_array.dat', dtype=np.float32, mode='w+', shape=(1000000, 1000000))
print(array.nbytes)
