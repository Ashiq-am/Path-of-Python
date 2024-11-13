# Function to draw a vertical line and add text
def annotate_plot(*args, **kwargs):
    for ax in g.axes.flat:
        # Draw a vertical line
        ax.axvline(x=20, color='r', linestyle='--')
        # Add text
        ax.text(22, 30, 'Threshold', color='red', fontsize=12, weight='bold', style='italic')

# Apply the function to the FacetGrid
g.map(annotate_plot)

plt.show()
