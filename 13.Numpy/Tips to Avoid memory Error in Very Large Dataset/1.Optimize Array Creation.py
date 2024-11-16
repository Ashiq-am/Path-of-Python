import numpy as np

# Example: Create a large array incrementally
size = 100000000  # 100 million elements
increment = 10000
large_array = np.array([], dtype=np.float64)
for i in range(0, size, increment):
    chunk = np.random.rand(increment)
    large_array = np.append(large_array, chunk)
print("Array created successfully with size:", large_array.size)
