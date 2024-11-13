# Create a heatmap with adjusted size
plt.figure(figsize=(10, 8))
sns.heatmap(data, annot=True, fmt="d", cmap="coolwarm")
plt.title("Heatmap with Adjusted Size")
plt.show()
