# Load necessary packages and functions
import scipy.stats as stats
import numpy as np

# Make a 3 x 3 table
dataset = np.array([[13, 17, 11], [4, 6, 9],
					[20, 31, 42]])

# Finding Chi-squared test statistic,
# sample size, and minimum of rows
# and columns
X2 = stats.chi2_contingency(dataset, correction=False)[0]
N = np.sum(dataset)
minimum_dimension = min(dataset.shape)-1

# Calculate Cramer's V
result = np.sqrt((X2/N) / minimum_dimension)

# Print the result
print(result)
