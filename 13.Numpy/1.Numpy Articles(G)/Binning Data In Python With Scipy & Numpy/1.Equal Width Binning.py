import numpy as np

# Generate some example data
data = np.random.rand(100)
# Define the number of bins
num_bins = 10
# Use numpy's histogram function for equal width bins
hist, bins = np.histogram(data, bins=num_bins)
print("Bin Edges:", bins)
print("Histogram Counts:", hist)
