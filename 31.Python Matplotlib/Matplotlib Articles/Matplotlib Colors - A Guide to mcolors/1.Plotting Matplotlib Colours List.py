import math
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
from matplotlib.patches import Rectangle


def plot_colortable(colors, *, ncols=4, sort_colors=True):
    # Define dimensions for each color cell and margins
    cell_width = 212
    cell_height = 22
    swatch_width = 48
    margin = 12

    # Sort colors by their HSV values (if sort_colors is True) for visual harmony
    if sort_colors:
        names = sorted(colors, key=lambda c: tuple(mcolors.rgb_to_hsv(mcolors.to_rgb(c))))
    else:

        # Use colors in their original order
        names = list(colors)

        # Calculate the number of rows needed based
    # on the number of colors and desired number of columns
    n = len(names)
    nrows = math.ceil(n / ncols)

    # Calculate figure size based on the
    # number of columns and rows, including margins
    width = cell_width * ncols + 2 * margin
    height = cell_height * nrows + 2 * margin
    dpi = 72  # Set figure DPI

    # Create figure and axis for drawing the color table
    fig, ax = plt.subplots(figsize=(width / dpi, height / dpi), dpi=dpi)
    fig.subplots_adjust(margin / width, margin / height, (width - margin) / width, (height - margin) / height)
    ax.set_xlim(0, cell_width * ncols)
    ax.set_ylim(cell_height * (nrows - 0.5), -cell_height / 2.)
    ax.yaxis.set_visible(False)  # Hide Y axis
    ax.xaxis.set_visible(False)  # Hide X axis
    ax.set_axis_off()  # Hide the axis border

    # Add color swatches and names to the figure
    for i, name in enumerate(names):
        row = i % nrows
        col = i // nrows
        y = row * cell_height

        swatch_start_x = cell_width * col  # X position for the swatch
        text_pos_x = cell_width * col + swatch_width + 7  # X position for the text

        # Add the color name text next to the swatch
        ax.text(text_pos_x, y, name, fontsize=14,
                horizontalalignment='left',
                verticalalignment='center')

        # Add the color swatch
        ax.add_patch(
            Rectangle(xy=(swatch_start_x, y - 9), width=swatch_width,
                      height=18, facecolor=colors[name], edgecolor='0.7')
        )

    return fig


# Example usage of the function
if __name__ == "__main__":
    # Define a sample set of colors by their names and corresponding color codes
    colors = {
        'b': 'blue',
        'g': 'green',
        'r': 'red',
        'c': 'cyan',
        'm': 'magenta',
        'y': 'yellow',
        'k': 'black',
    }

    # Call the function to plot the color table with these colors
    fig = plot_colortable(colors, ncols=3, sort_colors=False)
    plt.show()  # Display the plot
