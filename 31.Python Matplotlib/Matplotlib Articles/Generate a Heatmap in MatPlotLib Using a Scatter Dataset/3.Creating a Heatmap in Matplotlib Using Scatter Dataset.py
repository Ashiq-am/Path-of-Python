# Create a 2D histogram
heatmap, xedges, yedges = np.histogram2d(x, y, bins=50)

# Plot the heatmap
plt.imshow(heatmap.T, origin='lower', cmap='viridis', aspect='auto')
plt.colorbar(label='Density')
plt.title('Heatmap')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.show()
