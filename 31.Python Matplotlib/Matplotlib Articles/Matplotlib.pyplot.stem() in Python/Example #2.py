# importing libraries
import random
import matplotlib.pyplot as plt

x = np.linspace(0.1, 2 * np.pi, 41)
y = np.exp(np.sin(x))

markerline, stemlines, baseline = plt.stem(
	x, y, linefmt ='grey', markerfmt ='D',
	bottom = 1.1, use_line_collection = True)

markerline.set_markerfacecolor('none')
plt.show()
