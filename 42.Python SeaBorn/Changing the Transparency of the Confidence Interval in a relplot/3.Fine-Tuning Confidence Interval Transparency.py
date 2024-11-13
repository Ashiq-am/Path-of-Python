# Create the plot
g = sns.relplot(
    x="timepoint",
    y="signal",
    kind="line",
    data=data,
    ci=95  # Display confidence interval
)

# Access the underlying axes
ax = g.axes[0, 0]

# Get the confidence interval polygons and adjust transparency
for artist in ax.collections:
    artist.set_alpha(0.3)  # Adjust alpha for CI only

plt.show()
