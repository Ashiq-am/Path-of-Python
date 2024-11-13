# Function to add text
def add_text(*args, **kwargs):
    for ax in g.axes.flat:
        ax.text(25, 30, 'Threshold', color='red')

# Apply the function to the FacetGrid
g.map(add_text)

plt.show()
