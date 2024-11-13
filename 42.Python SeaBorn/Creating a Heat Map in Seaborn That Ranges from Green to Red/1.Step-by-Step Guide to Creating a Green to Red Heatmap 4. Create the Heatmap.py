# Create the heatmap
plt.figure(figsize=(10, 8))
sns.heatmap(df, cmap=cm, annot=True, fmt=".2f", linewidths=.5)
plt.title('Green to Red Heatmap')
plt.show()
