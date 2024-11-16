# Load necessary packages and functions
import scipy.stats as stats
import numpy as np

# Make a 5 x 4 table
dataset = np.array([[4, 13, 17, 11], [4, 6, 9, 12],
					[2, 7, 4, 2], [5, 13, 10, 12],
					[5, 6, 14, 12]])

# Finding Chi-squared test statistic,
# sample size, and minimum of rows and
# columns
X2 = stats.chi2_contingency(dataset, correction=False)[0]
N = np.sum(dataset)
minimum_dimension = min(dataset.shape)-1

# Calculate Cramer's V
result = np.sqrt((X2/N) / minimum_dimension)

# Print the result
print(result)
