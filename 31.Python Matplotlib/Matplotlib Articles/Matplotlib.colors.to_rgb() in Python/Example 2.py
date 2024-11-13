from matplotlib import colors
import matplotlib.pyplot as plt


alpha = 0.5

kwargs = dict(edgecolors ='none', s = 3900, marker ='s')

for i, color in enumerate(['pink', 'brown', 'green']):

	rgb = colors.to_rgb(color)
	plt.scatter([i], [0], color = color, **kwargs)
	plt.scatter([i], [1], color = color,
				alpha = alpha, **kwargs)
	plt.scatter([i], [2], color = rgb, **kwargs)
