# Create violin plot
vp = plt.violinplot(data)

# Change face color and add transparency
for body in vp['bodies']:
    body.set_facecolor('lightblue')
    body.set_alpha(0.5)  # Set transparency to 50%

plt.show()
