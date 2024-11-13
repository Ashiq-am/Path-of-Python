# Calculate the best-fit line
z = np.polyfit(x, y, 1)
p = np.poly1d(z)

# Plot the scatter plot and the trend line
plt.scatter(x, y)
plt.plot(x, p(x), "r--")  # 'r--' is for a red dashed line
plt.title("Scatter Plot with Linear Trend Line")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.show()
