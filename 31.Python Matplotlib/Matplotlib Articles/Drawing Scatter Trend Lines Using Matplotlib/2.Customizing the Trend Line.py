# Calculate the best-fit line
z = np.polyfit(x, y, 1)
p = np.poly1d(z)

# Plot the scatter plot and the customized trend line
plt.scatter(x, y)
plt.plot(x, p(x), color="purple", linewidth=2, linestyle="--")
plt.title("Scatter Plot with Customized Trend Line")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.show()
