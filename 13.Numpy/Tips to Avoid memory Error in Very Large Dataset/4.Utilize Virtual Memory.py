import numpy as np

# Example: Memory-mapped array
filename = 'large_array.npy'
large_array_mmapped = np.memmap(filename, dtype='float32', mode='w+', shape=(100000000,))
large_array_mmapped[:] = np.random.rand(100000000)  # Writing data to disk
del large_array_mmapped  # Freeing memory
large_array_mmapped = np.memmap(filename, dtype='float32', mode='r', shape=(100000000,))
print(large_array_mmapped[:10])  # Accessing data from disk
