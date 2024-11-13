# Generate random data points
np.random.seed(0)
x = np.random.randn(1000)
y = np.random.randn(1000)

# Create a scatter plot
plt.scatter(x, y, alpha=0.5)
plt.title('Scatter Plot')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.show()
