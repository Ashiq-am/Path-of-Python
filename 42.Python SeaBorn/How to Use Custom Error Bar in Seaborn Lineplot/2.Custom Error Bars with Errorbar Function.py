# Create a sample dataset
np.random.seed(10)
x = np.linspace(0, 10, 10)
y = np.sin(x) + np.random.normal(0, 0.1, 10)
data = pd.DataFrame({'x': x, 'y': y})

# Compute custom error values
error = np.random.normal(0.1, 0.02, size=y.shape)

# Plot the lineplot
ax = sns.lineplot(x='x', y='y', data=data)

# Add custom error bars using errorbar
ax.errorbar(x, y, yerr=error, fmt='o', color='b', alpha=0.5)

plt.show()
