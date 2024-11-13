# Create a 2D histogram
heatmap, xedges, yedges = np.histogram2d(x, y, bins=50)

# Plot the heatmap with annotations
sns.heatmap(heatmap.T, cmap='viridis', annot=True, fmt='.1f')
plt.title('Heatmap with Annotations')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.show()
