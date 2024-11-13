# Python Program illustrating
# pyplot.colorbar() method
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt

x = np.linspace(0, 5, 100)
N = 7

# colormap
cmap = plt.get_cmap('jet', N)

fig, ax1 = plt.subplots(1, 1, figsize=(8, 6))

for i, n in enumerate(np.linspace(0, 2, N)):
	y = x*i+n
	ax1.plot(x, y, c=cmap(i))

plt.xlabel('x-axis')
plt.ylabel('y-axis')

# Normalizer
norm = mpl.colors.Normalize(vmin=0, vmax=2)

# creating ScalarMappable
sm = plt.cm.ScalarMappable(cmap=cmap, norm=norm)
sm.set_array([])

plt.colorbar(sm, ticks=np.linspace(0, 2, N))


plt.show()
