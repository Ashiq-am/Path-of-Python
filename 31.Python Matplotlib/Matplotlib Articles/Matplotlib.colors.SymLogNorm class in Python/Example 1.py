import numpy as np
import matplotlib.pyplot as plt
import matplotlib.colors as colors


# SymLogNorm: two humps, one
# negative and one positive
N = 100
A, B = np.mgrid[-3:3:complex(0, N), -2:2:complex(0, N)]
C1 = np.exp(-A**2 - B**2)
C2 = np.exp(-(A - 1)**2 - (B - 1)**2)
C = (C1 - C2) * 2

figure, axes = plt.subplots(2, 1)

pcm = axes[0].pcolormesh(A, B, C,
					norm = colors.SymLogNorm(linthresh = 0.03,
												linscale = 0.03,
												vmin =-1.0,
												vmax = 1.0),
					cmap ='RdBu_r')

figure.colorbar(pcm, ax = axes[0], extend ='both')

pcm = axes[1].pcolormesh(A, B, C,
						cmap ='RdBu_r',
						vmin =-np.max(C))

figure.colorbar(pcm, ax = axes[1],
				extend ='both')

plt.show()
