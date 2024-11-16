import numpy as np

# Generate some example data
data = np.random.rand(100)

# Define custom bin edges
bin_edges = [0, 0.2, 0.4, 0.6, 0.8, 1.0]

# Use numpy's histogram function with custom bins
hist, bins = np.histogram(data, bins=bin_edges)

# Print the result
print("Bin Edges:", bins)
print("Histogram Counts:", hist)
