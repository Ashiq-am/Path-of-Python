import random
import statistics
from scipy.stats import binned_statistic

# Generate some example data
data = [random.random() for _ in range(100)]

# Define the number of bins
num_bins = 10

# Use binned_statistic to calculate mean within each bin
result = binned_statistic(data, data, bins=num_bins, statistic='mean')

# Extract bin edges and binned mean from the result
bin_edges = result.bin_edges
bin_means = result.statistic

# Print the result
print("Bin Edges:", bin_edges)
print("Binned Mean:", bin_means)
