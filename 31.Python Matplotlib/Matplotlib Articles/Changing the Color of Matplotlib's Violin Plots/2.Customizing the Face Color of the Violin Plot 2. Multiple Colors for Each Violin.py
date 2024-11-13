colors = ['lightblue', 'lightgreen', 'lightcoral', 'lightpink']

# Create violin plot
vp = plt.violinplot(data)

# Change face color for each violin
for i, body in enumerate(vp['bodies']):
    body.set_facecolor(colors[i])

plt.show()
