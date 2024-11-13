import matplotlib.pyplot as plt
from matplotlib.patches import ArrowStyle

plt.figure(1, figsize =(9, 9))

ArrowStyle("Wedge")

ax = plt.subplot(111)

ax.annotate("",
			xy =(0.2, 0.2), xycoords ='data',
			xytext =(0.8, 0.8), textcoords ='data',
			arrowprops = dict(arrowstyle ="Wedge",
							connectionstyle ="arc3"),
			)

plt.show()
