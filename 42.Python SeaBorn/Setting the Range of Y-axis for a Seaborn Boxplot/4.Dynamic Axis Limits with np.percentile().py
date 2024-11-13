import numpy as np

# Calculate 5th and 95th percentiles
lower_bound = np.percentile(data['total_bill'], 5)
upper_bound = np.percentile(data['total_bill'], 95)

# Set the y-axis range to the central 90% of data
plt.ylim(lower_bound, upper_bound)
