# Creating the contour plot with contour lines
contour = plt.contour(X, Y, Z, levels=10, cmap='viridis')

# Adding contour labels
plt.clabel(contour, inline=True, fontsize=8)

# Adding labels and title
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('Contour Plot with Contour Labels')

# Display the plot
plt.show()
