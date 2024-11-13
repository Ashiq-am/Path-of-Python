import matplotlib.pyplot as plt
import numpy as np
from matplotlib.colors import LogNorm


N = 100
A, B = np.mgrid[-3:3:complex(0, N),
				-2:2:complex(0, N)]

X1 = np.exp(-(A)**2 - (B)**2)
X2 = np.exp(-(A * 10)**2 - (B * 10)**2)
X = X1 + 50 * X2

figure, (axes0, axes1) = plt.subplots(2, 1)

P = axes0.pcolor(A, B, X,
			norm = LogNorm(vmin = X.min(),
							vmax = X.max()),
				cmap ='PuBu_r')

figure.colorbar(P, ax = axes0)

P = axes1.pcolor(A, B, X,
				cmap ='PuBu_r')

figure.colorbar(P, ax = axes1)

plt.show()
