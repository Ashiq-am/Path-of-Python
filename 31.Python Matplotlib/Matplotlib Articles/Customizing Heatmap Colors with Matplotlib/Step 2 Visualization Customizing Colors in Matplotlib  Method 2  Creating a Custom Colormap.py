# Method 2: Creating a Custom Colormap
colors = ["#ff0000", "#ffff00", "#00ff00", "#00ffff", "#0000ff"]  # Define custom colors
custom_cmap = LinearSegmentedColormap.from_list("custom_cmap", colors)  # Create custom colormap
plt.subplot(232)
plt.imshow(data, cmap=custom_cmap)
plt.colorbar()
plt.title('Custom Colormap')
plt.show()
