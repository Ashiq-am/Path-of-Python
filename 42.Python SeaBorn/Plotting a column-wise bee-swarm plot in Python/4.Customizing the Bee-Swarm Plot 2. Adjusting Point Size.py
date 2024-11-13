# Customizing Point Size
fig, axes = plt.subplots(2, 2, figsize=(12, 10))

# Sepal Length
sns.swarmplot(ax=axes[0, 0], x='species', y='sepal_length', data=df, size=10)
axes[0, 0].set_title('Sepal Length by Species')

# Sepal Width
sns.swarmplot(ax=axes[0, 1], x='species', y='sepal_width', data=df, size=8)
axes[0, 1].set_title('Sepal Width by Species')

# Petal Length
sns.swarmplot(ax=axes[1, 0], x='species', y='petal_length', data=df, size=6)
axes[1, 0].set_title('Petal Length by Species')

# Petal Width
sns.swarmplot(ax=axes[1, 1], x='species', y='petal_width', data=df, size=4)
axes[1, 1].set_title('Petal Width by Species')

plt.tight_layout()
plt.show()
