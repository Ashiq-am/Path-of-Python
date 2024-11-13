# Implementation of matplotlib function

import numpy as np
import matplotlib.pyplot as plt

y = np.arange(0.0, 2, 0.01)
x1 = np.sin(2 * np.pi * y)
x2 = 0.8 * np.sin(4 * np.pi * y)

fig, [ax1, ax2, ax3, ax4] = plt.subplots(1, 4,sharey=True,figsize=(6, 6))

ax1.fill_betweenx(y, 0, x1, facecolor='green')
ax1.set_title('Fill_Betweenx x1 and 0')

ax2.fill_betweenx(y, x1, 1, facecolor='green')
ax2.set_title('Fill_Betweenx x1 and 1')

ax3.fill_betweenx(y, x1, x2, facecolor='green')
ax3.set_title('Fill_Betweenx x1 and y2')

ax4.fill_betweenx(y, x1, x2, where=x2 <= x1,
                  facecolor='green')

ax4.set_title('Fill_Between x1 and x2 with x2<= x1 ')
plt.show()
