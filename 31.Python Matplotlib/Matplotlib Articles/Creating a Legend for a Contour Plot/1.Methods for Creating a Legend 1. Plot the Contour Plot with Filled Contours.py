# Creating the contour plot with filled contours
contour = plt.contourf(X, Y, Z, levels=10, cmap='viridis')

# Adding a color bar
cbar = plt.colorbar(contour)
cbar.set_label('Z-value')

# Adding labels and title
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('Contour Plot with Color Bar')

# Display the plot
plt.show()
