import numpy as np

# Generate some example data
data = np.random.rand(100)

# Define bin edges using linspace
bin_edges = np.linspace(0, 1, 6) # Create 5 bins from 0 to 1

# Bin the data using digitize
bin_indices = np.digitize(data, bin_edges)

# Calculate histogram counts using bin count
hist = np.bincount(bin_indices)
print("Bin Edges:", bin_edges)
print("Histogram Counts:", hist)
