# Function to draw a vertical line
def draw_vline(*args, **kwargs):
    for ax in g.axes.flat:
        ax.axvline(x=20, color='r', linestyle='--')

# Apply the function to the FacetGrid
g.map(draw_vline)

plt.show()
