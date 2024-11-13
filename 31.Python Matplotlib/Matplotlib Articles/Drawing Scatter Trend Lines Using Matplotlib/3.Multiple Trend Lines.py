# Generate random data
x = np.random.rand(50)
y = np.random.rand(50)

# Calculate the linear and polynomial trend lines
z1 = np.polyfit(x, y, 1)
p1 = np.poly1d(z1)
z2 = np.polyfit(x, y, 2)
p2 = np.poly1d(z2)

# Plot the scatter plot and both trend lines
plt.scatter(x, y)
plt.plot(x, p1(x), "r--", label="Linear Trend Line")
plt.plot(x, p2(x), "g-", label="Polynomial Trend Line")
plt.title("Scatter Plot with Multiple Trend Lines")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.legend()
plt.show()
