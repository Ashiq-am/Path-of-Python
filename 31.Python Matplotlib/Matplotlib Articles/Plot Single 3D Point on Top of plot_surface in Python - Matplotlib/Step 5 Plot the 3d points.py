fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

ax.scatter(point_x, point_y, point_z, color='red', s=50)

# Customize the plot (add labels, titles, etc.)
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.set_title('Single Point in 3D')

# Adjust the viewing perspective if needed
ax.view_init(elev=20, azim=45)

# Show the plot
plt.show()
