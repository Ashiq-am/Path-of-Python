import numpy as np
import matplotlib.pyplot as plt

# Fixing random state for
# reproducibility
np.random.seed(19680801)

# the random data
x = np.random.randn(1000)
y = np.random.randn(1000)

# definitions for the axes
left, width = 0.1, 0.65
bottom, height = 0.1, 0.65
spacing = 0.005


rect_scatter = [left, bottom,
				width, height]

rect_histx = [left,
			bottom + height + spacing,
			width, 0.2]

rect_histy = [left + width + spacing,
			bottom, 0.2, height]

# start with a rectangular Figure
plt.figure()

ax_scatter = plt.axes(rect_scatter)
ax_scatter.tick_params(direction ='in',
					bottom = True,
					right = True)

ax_histx = plt.axes(rect_histx)
ax_histx.tick_params(direction ='in',
					labeltop = True)

ax_histy = plt.axes(rect_histy)
ax_histy.tick_params(direction ='in',
					labelleft = True)


# the scatter plot:
ax_scatter.scatter(2 * x, y * 2, color ="green")

# now determine nice limits by hand:
binwidth = 0.05
lim = np.ceil(np.abs([x, y]).max() / binwidth) * binwidth
ax_scatter.set_xbound((-0.5 * lim, 0.5 * lim))
ax_scatter.set_ybound((-0.25 * lim, 0.25 * lim))

bins = np.arange(-lim, lim + binwidth, binwidth)
ax_histx.hist(x, bins = bins,
			color ="green")
ax_histy.hist(y, bins = bins,
			color ="green",
			orientation ='horizontal')

ax_histx.set_xbound(ax_scatter.get_xbound())
ax_histy.set_ybound(ax_scatter.get_ybound())

plt.show()
