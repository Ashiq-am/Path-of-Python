# Create the polar scatter plot with offset origin
plt.figure(figsize=(8, 8))
ax = plt.subplot(111, polar=True, theta_offset=np.pi/4) # Offset origin by pi/4
ax.scatter(theta, r, c=colors, s=100, cmap='hsv', alpha=0.75)

plt.title('Scatter Plot on Polar Axis with Offset Origin', fontsize=15)
plt.show()
