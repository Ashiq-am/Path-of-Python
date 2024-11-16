import numpy as np
# Smaller data type (float32)
array = np.ones((100000, 100000), dtype=np.dtype(np.float32))
print(array.nbytes)
