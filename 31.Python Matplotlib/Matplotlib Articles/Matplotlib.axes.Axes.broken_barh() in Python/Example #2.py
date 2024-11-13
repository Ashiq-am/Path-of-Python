# Implementation of matplotlib function
import matplotlib.pyplot as plt

fig, ax = plt.subplots()
ax.broken_barh([(110, 30), (150, 10)],
			(10, 9),
			facecolors ='tab:green')

ax.broken_barh([(100, 20),
				(130, 10)],
			(20, 9),
			facecolors =('tab:green'))

ax.set_ylim(5, 35)
ax.set_xlim(50, 200)
ax.set_xlabel('Learning Rate')
ax.set_yticks([15, 25])
ax.set_yticklabels(['Geeks1', 'Geeks2'])
ax.grid(True)

ax.annotate('Broken', (125, 25),
			xytext =(0.8, 0.9),
			textcoords ='axes fraction',
			arrowprops = dict(facecolor ='black',
							shrink = 0.05),
			fontsize = 16,
			horizontalalignment ='right',
			verticalalignment ='top')

ax.set_title('matplotlib.axes.Axes.broken_barh Example')

plt.show()
