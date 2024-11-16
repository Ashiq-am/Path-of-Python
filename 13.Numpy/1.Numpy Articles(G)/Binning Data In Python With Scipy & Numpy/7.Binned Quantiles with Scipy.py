from scipy.stats import binned_statistic

# Generate some example data
data = np.random.randn(1000)

# Define the number of bins
num_bins = 20

# Use binned_statistic to calculate quantiles within each bin
result = binned_statistic(data, data, bins=num_bins, statistic=lambda x: np.percentile(x, q=75))

# Print the result
print("Bin Edges:", result.bin_edges)
print("75th Percentile within Each Bin:", result.statistic)
