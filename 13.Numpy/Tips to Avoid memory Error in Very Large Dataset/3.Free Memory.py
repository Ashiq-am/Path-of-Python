import numpy as np

# Example: Free memory occupied by unused variables
large_array = np.random.rand(100000000)  # Large array of 100 million elements
# Process large_array
del large_array  # Free memory
