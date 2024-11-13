# Create violin plot
vp = plt.violinplot(data)

# Change face color
for body in vp['bodies']:
    body.set_facecolor('lightblue')

plt.show()
