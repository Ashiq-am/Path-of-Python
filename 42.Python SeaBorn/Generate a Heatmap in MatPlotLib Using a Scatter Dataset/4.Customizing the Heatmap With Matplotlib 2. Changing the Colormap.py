# Plot the heatmap with a different colormap
plt.imshow(heatmap.T, origin='lower', cmap='plasma', aspect='auto')
plt.colorbar(label='Density')
plt.title('Heatmap with Plasma Colormap')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.show()
