import matplotlib.pyplot as plt
import numpy as np
from matplotlib.ticker import MaxNLocator

x = np.linspace(-3.0, 3.0, 100)
y = np.linspace(-3.0, 3.0, 100)
X, Y = np.meshgrid(x, y)
Z = np.sin(X) * np.cos(Y)

fig, ax = plt.subplots()
cax = ax.contourf(X, Y, Z, cmap='viridis')

cbar = fig.colorbar(cax)

cbar.locator = MaxNLocator(nbins=5)
cbar.update_ticks()

cbar.set_label('Sine-Cosine Value', rotation=270, labelpad=15)

plt.title('Contour Plot with Automatic Number of Ticks')
plt.show()
