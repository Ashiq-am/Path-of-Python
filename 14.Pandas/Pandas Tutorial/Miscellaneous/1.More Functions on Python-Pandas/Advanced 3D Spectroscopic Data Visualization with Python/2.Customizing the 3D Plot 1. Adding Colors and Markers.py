# Define colors and markers
colors = ['r', 'g', 'b', 'c', 'm', 'y', 'k']
markers = ['o', '^', 's', 'p', '*', 'x', 'D']

# Plot the data with colors and markers
for i, (sample, measurements) in enumerate(data.items()):
    x = np.full_like(measurements, i)
    y = np.arange(len(measurements))
    z = measurements
    ax.plot(x, y, z, color=colors[i % len(colors)], marker=markers[i % len(markers)], label=sample)

# Show the plot
plt.show()
