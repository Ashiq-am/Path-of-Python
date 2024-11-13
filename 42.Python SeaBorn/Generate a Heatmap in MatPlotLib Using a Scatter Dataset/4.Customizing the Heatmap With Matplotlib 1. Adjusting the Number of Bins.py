# Create a 2D histogram with more bins
heatmap, xedges, yedges = np.histogram2d(x, y, bins=100)

# Plot the heatmap
plt.imshow(heatmap.T, origin='lower', cmap='viridis', aspect='auto')
plt.colorbar(label='Density')
plt.title('Heatmap with More Bins')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.show()
