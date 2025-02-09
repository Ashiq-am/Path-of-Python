# Creating two arrays for correlation and covariance
x = np.array([1, 2, 3, 4, 5])
y = np.array([2, 4, 6, 8, 10])

# Calculating correlation coefficient matrix
correlation_matrix = np.corrcoef(x, y)
print("Correlation Coefficient Matrix:\n", correlation_matrix)

# Calculating covariance matrix
covariance_matrix = np.cov(x, y)
print("Covariance Matrix:\n", covariance_matrix)