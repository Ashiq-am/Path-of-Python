import numpy as np

# Example: Process large array in chunks
large_array = np.random.rand(10000000)  # Large array of 10 million elements
chunk_size = 10000
num_chunks = len(large_array) // chunk_size
for i in range(num_chunks):
    chunk = large_array[i * chunk_size: (i + 1) * chunk_size]
    # Process chunk here
    print("Processed chunk", i)
