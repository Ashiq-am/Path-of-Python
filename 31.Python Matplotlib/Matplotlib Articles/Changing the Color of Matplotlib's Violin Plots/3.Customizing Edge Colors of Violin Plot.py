# Create violin plot
vp = plt.violinplot(data)

# Change face and edge color
for body in vp['bodies']:
    body.set_facecolor('lightblue')
    body.set_edgecolor('blue')  # Set edge color to blue

plt.show()
