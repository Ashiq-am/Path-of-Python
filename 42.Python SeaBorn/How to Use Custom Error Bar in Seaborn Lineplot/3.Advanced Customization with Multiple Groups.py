# Create a sample dataset with multiple groups
np.random.seed(10)
x = np.linspace(0, 10, 100)
y1 = np.sin(x) + np.random.normal(0, 0.1, 100)
y2 = np.cos(x) + np.random.normal(0, 0.1, 100)
data = pd.DataFrame({'x': np.concatenate([x, x]),
                     'y': np.concatenate([y1, y2]),
                     'group': ['A']*100 + ['B']*100})

# Compute custom error values for each group
error1 = np.random.normal(0.1, 0.02, size=y1.shape)
lower1 = y1 - error1
upper1 = y1 + error1

error2 = np.random.normal(0.1, 0.02, size=y2.shape)
lower2 = y2 - error2
upper2 = y2 + error2

# Plot the lineplot with multiple groups
ax = sns.lineplot(x='x', y='y', hue='group', data=data)

# Add custom error bars for each group
ax.fill_between(x, lower1, upper1, color='b', alpha=0.2)
ax.fill_between(x, lower2, upper2, color='r', alpha=0.2)

plt.show()
