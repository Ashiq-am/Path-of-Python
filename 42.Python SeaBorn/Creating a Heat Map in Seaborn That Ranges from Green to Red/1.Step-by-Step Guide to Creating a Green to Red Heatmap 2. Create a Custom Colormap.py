# Define the colormap
colors = [(0, 1, 0), (1, 1, 1), (1, 0, 0)]  # Green -> White -> Red
n_bins = 100  # Discretize the interpolation into bins
cmap_name = 'green_red'
cm = LinearSegmentedColormap.from_list(cmap_name, colors, N=n_bins)
