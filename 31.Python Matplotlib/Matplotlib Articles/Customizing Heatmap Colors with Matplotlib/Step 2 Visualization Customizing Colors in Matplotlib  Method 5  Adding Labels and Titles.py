# Method 5: Adding Labels and Titles
plt.subplot(235)
plt.imshow(data, cmap='inferno')
plt.colorbar()
plt.title('Heatmap with Labels')
plt.xlabel('X Axis')
plt.ylabel('Y Axis')
plt.show()
