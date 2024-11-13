colors = ['lightblue', 'lightgreen', 'lightcoral', 'lightpink']
edge_colors = ['blue', 'green', 'red', 'purple']

# Create violin plot
vp = plt.violinplot(data, showmeans=True)

# Customize each violin
for i, body in enumerate(vp['bodies']):
    body.set_facecolor(colors[i])
    body.set_edgecolor(edge_colors[i])
    body.set_alpha(0.7)  # Set transparency

# Customize mean line
vp['cmeans'].set_color('black')    # Change mean line color to black
vp['cmeans'].set_linestyle('--')   # Dashed line for the mean

plt.show()
