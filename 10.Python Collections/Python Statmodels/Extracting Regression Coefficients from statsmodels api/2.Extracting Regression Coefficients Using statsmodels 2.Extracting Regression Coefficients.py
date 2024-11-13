# Extract coefficients
coefficients = results.params
print("Intercept:", coefficients['const'])
print("Slope:", coefficients['X'])
# Print the summary of the regression model
print(results.summary())
