# Create violin plot
vp = plt.violinplot(data, showmeans=True)

# Customizing the mean line
vp['cmeans'].set_color('red')   # Change the mean line to red
vp['cmeans'].set_linestyle('--') # Set the line style to dashed

plt.show()
