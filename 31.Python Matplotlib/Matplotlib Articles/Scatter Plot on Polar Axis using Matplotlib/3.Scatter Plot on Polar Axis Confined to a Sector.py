# Create the polar scatter plot confined to a sector
plt.figure(figsize=(8, 8))
ax = plt.subplot(111, polar=True)
ax.scatter(theta, r, c=colors, s=100, cmap='hsv', alpha=0.75)

# Confine scatter plot to a sector
ax.set_thetamin(45) # Minimum theta angle
ax.set_thetamax(135) # Maximum theta angle

plt.title('Scatter Plot on Polar Axis Confined to a Sector', fontsize=15)
plt.show()
