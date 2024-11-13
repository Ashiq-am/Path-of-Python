# Implementation of matplotlib function
import matplotlib
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec


fig = plt.figure()
gs = fig.add_gridspec(3, 3)
ax = fig.add_subplot(gs[0, :])

ax.set_title('gs[0, :]')
ax2 = fig.add_subplot(gs[1, :-1])
ax2.set_title('gs[1, :-1]')

fig.set_constrained_layout(False)

fig.suptitle("""matplotlib.figure.Figure.set_constrained_layout() 
function Example\n\n""", fontweight ="bold")

plt.show()
