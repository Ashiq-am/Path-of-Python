import numpy as np
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D

# Draw 5 points for each line
each_point = np.ones(5)
style = dict(color='tab:green',
             linestyle=':',
             marker='D',
             markersize=15,
             markerfacecoloralt='tab:red')

figure, axes = plt.subplots()

# Plot all filling styles.
for y, fill_style in enumerate(Line2D.fillStyles):
    axes.text(-0.5, y,
              repr(fill_style),
              horizontalalignment='center',
              verticalalignment='center')

    axes.plot(y * each_point, fillstyle=fill_style,
              **style)

axes.set_axis_off()
axes.set_title('filling style')

plt.show()
