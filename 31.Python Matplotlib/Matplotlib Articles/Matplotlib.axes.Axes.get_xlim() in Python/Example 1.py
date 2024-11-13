#Implementation of matplotlib function
from matplotlib.widgets import Cursor
import numpy as np
import matplotlib.pyplot as plt


np.random.seed(19680801)

fig, (ax,ax1) = plt.subplots(1 , 2 , facecolor='#A0F0CC')

x, y = 4*(np.random.rand(2, 100) - .5)
ax.plot(x, y, 'g')
ax.set_xlim(-3, 3)

xmin, xmax = ax.get_xlim()
ax.set_title('Original Window', fontsize=10, fontweight='bold')

ax1.plot(x, y, 'g')
ax1.set_xlim(xmin, 2*xmax)
ax1.set_title('Using get_xlim() function',
			fontsize=10, fontweight='bold')

fig.suptitle('matplotlib.axes.Axes.get_xlim() Example\n',fontsize=10, fontweight='bold')
plt.show()
