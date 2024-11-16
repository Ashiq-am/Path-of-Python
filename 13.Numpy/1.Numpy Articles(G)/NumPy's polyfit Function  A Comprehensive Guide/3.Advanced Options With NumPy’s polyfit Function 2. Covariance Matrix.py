# Perform fit with covariance
coefficients, cov_matrix = np.polyfit(x, y, 1, cov=True)
print("Fit Coefficients:", coefficients)
print("Covariance Matrix:", cov_matrix)
