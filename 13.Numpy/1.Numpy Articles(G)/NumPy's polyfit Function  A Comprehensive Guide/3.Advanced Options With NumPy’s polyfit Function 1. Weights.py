# Weights
weights = np.array([1, 1, 1, 1, 1, 10])

# Perform weighted fit
coefficients_weighted = np.polyfit(x, y, 1, w=weights)
print("Weighted Fit Coefficients:", coefficients_weighted)
