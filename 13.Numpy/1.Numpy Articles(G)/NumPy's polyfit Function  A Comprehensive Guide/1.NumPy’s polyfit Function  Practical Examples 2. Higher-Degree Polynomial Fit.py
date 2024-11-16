# Perform cubic fit
coefficients = np.polyfit(x, y, 3)
print("Cubic Fit Coefficients:", coefficients)

# Create polynomial function
p = np.poly1d(coefficients)

# Plot data and fit
xp = np.linspace(-1, 6, 100)
plt.scatter(x, y, label='Data Points')
plt.plot(xp, p(xp), label='Cubic Fit', color='green')
plt.legend()
plt.show()
