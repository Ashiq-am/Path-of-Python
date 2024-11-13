from scipy.optimize import curve_fit

# Perform curve fitting
popt, pcov = curve_fit(func, (x, y), z)

# Print optimized parameters
print(popt)
