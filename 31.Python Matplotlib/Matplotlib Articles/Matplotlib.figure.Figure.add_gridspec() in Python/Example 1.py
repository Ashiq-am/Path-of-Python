# Implementation of matplotlib function
import matplotlib
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec


fig = plt.figure(constrained_layout = True)
gs = fig.add_gridspec(3, 3)
ax = fig.add_subplot(gs[0, :])
ax.set_title('gs[0, :]')
ax2 = fig.add_subplot(gs[1, :-1])
ax2.set_title('gs[1, :-1]')


fig.suptitle('matplotlib.figure.Figure.add_gridspec() function Example\n\n', fontweight ="bold")

plt.show()
