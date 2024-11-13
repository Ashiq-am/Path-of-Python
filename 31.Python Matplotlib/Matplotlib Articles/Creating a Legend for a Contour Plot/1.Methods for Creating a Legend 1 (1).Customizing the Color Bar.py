# Creating the contour plot with filled contours
contour = plt.contourf(X, Y, Z, levels=10, cmap='viridis')

# Adding a customized color bar
cbar = plt.colorbar(contour, orientation='horizontal', pad=0.1, shrink=0.8)
cbar.set_label('Z-value', rotation=0, labelpad=10)

# Adding labels and title
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('Contour Plot with Customized Color Bar')

# Display the plot
plt.show()
