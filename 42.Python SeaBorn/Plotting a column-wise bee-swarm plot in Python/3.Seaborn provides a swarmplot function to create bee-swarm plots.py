# Create a figure with subplots for each column
fig, axes = plt.subplots(2, 2, figsize=(12, 10))

# Create bee-swarm plots for each feature
sns.swarmplot(ax=axes[0, 0], x='species', y='sepal_length', data=df)
axes[0, 0].set_title('Sepal Length by Species')

sns.swarmplot(ax=axes[0, 1], x='species', y='sepal_width', data=df)
axes[0, 1].set_title('Sepal Width by Species')

sns.swarmplot(ax=axes[1, 0], x='species', y='petal_length', data=df)
axes[1, 0].set_title('Petal Length by Species')

sns.swarmplot(ax=axes[1, 1], x='species', y='petal_width', data=df)
axes[1, 1].set_title('Petal Width by Species')

plt.tight_layout()
plt.show()
