# Calculate the polynomial trend line (degree 2)
z = np.polyfit(x, y, 2)
p = np.poly1d(z)

# Plot the scatter plot and the polynomial trend line
plt.scatter(x, y)
plt.plot(x, p(x), "g-")  # 'g-' is for a green solid line
plt.title("Scatter Plot with Polynomial Trend Line")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.show()
