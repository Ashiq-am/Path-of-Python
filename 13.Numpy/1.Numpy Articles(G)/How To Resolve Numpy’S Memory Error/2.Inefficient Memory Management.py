import numpy as np

# Inefficient memory usage leading to fragmentation
for _ in range(100000000000):
	large_array = np.ones((100000, 1000), dtype=np.float64)
