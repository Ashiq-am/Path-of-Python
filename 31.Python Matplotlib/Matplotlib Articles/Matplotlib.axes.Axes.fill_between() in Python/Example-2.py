# Implementation of matplotlib function

import numpy as np
import matplotlib.pyplot as plt

x = np.arange(0.0, 2, 0.01)
y1 = np.sin(2 * np.pi * x)
y2 = 0.8 * np.sin(4 * np.pi * x)

fig, (ax1, ax2, ax3, ax4) = plt.subplots(4, 1,
                                         sharex=True,
                                         figsize=(6, 6))

ax1.fill_between(x, y1, facecolor='green')
ax1.set_title('Fill_Between y1 and 0')

ax2.fill_between(x, y1, 1, facecolor='green')
ax2.set_title('Fill_Between y1 and 1')

ax3.fill_between(x, y1, y2, facecolor='green')
ax3.set_title('Fill_Between y1 and y2')
ax3.set_xlabel('x')
fig.tight_layout()

ax4.fill_between(x, y1, y2, where=y2 <= y1,
                 facecolor='green')

ax4.set_title('Fill_Between y1 and y2 with condition y2 <= y1 ')
ax4.set_xlabel('x')
fig.tight_layout()

plt.show()
