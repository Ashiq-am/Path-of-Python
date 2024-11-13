# Customizing Transparency with Alpha
fig, axes = plt.subplots(2, 2, figsize=(12, 10))

# Sepal Length
sns.swarmplot(ax=axes[0, 0], x='species', y='sepal_length', data=df, alpha=0.9)
axes[0, 0].set_title('Sepal Length by Species')

# Sepal Width
sns.swarmplot(ax=axes[0, 1], x='species', y='sepal_width', data=df, alpha=0.7)
axes[0, 1].set_title('Sepal Width by Species')

# Petal Length
sns.swarmplot(ax=axes[1, 0], x='species', y='petal_length', data=df, alpha=0.6)
axes[1, 0].set_title('Petal Length by Species')

# Petal Width
sns.swarmplot(ax=axes[1, 1], x='species', y='petal_width', data=df, alpha=0.8)
axes[1, 1].set_title('Petal Width by Species')

plt.tight_layout()
plt.show()
