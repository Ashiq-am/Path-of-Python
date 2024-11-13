edge_colors = ['blue', 'green', 'red', 'purple']

# Create violin plot
vp = plt.violinplot(data)

# Change face and edge color for each violin
for i, body in enumerate(vp['bodies']):
    body.set_facecolor(colors[i])
    body.set_edgecolor(edge_colors[i])

plt.show()
