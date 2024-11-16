from scipy.stats import binned_statistic

# Generate some example data
data = np.random.rand(100)

# Define the number of bins
num_bins = 10

# Use binned_statistic to calculate sum within each bin
result = binned_statistic(data, data, bins=num_bins, statistic='sum')

# Print the result
print("Bin Edges:", result.bin_edges)
print("Binned Sum:", result.statistic)
