import matplotlib.pyplot as plt
import numpy as np

fig, ax = plt.subplots(2, 2)
fig.suptitle('** Main Title for all sub plots **', fontsize=20)
plt.style.use('seaborn')

labels = ['first line', 'second line',
		'third line', 'fourth line', 'fifth line']

ax[0, 0].plot([1, 2, 3, 4, 5], [9, 3, 5, 7, 9], '-.', color='g')
ax[0, 0].set_title('first subplot')
ax[0, 0].set_yticks(np.arange(1, 10))

ax[0, 1].plot([1, 2, 3, 4, 5, 6], [1, 4, 9, 7, 9, 8], '-*', color='m')
ax[0, 1].set_title('second subplot')
ax[0, 1].set_yticks(np.arange(1, 10))

ax[1, 0].plot([1, 2, 3, 4, 5], [8, 5, 2, 3, 3], '-v', color='r')
ax[1, 0].set_title('third subplot')
ax[1, 0].set_yticks(np.arange(1, 9))

ax[1, 1].plot([1, 2, 3, 4, 5, 6], [1, 3, 5, 7, 9, 6], 'o-', color='b')
ax[1, 1].plot([1, 2, 3, 4, 5, 6, 7, 7], [
			7, 8, 6, 5, 2, 2, 4, 6], 'o-', color='g')
ax[1, 1].set_title('fourth subplot')
ax[1, 1].set_yticks(np.arange(1, 10))

fig.tight_layout()
fig.legend(ax, labels=labels, loc="upper right", borderaxespad=0.1)
fig.subplots_adjust(top=0.85)

plt.show()
