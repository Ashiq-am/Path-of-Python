import numpy as np
import matplotlib.pyplot as plt
import matplotlib.colors as colors

max_N = 100
A, B = np.mgrid[-3:3:complex(0, max_N),
				-2:2:complex(0, max_N)]


# PowerNorm: using power-law
# trend in X
A, B = np.mgrid[0:3:complex(0, max_N),
				0:2:complex(0, max_N)]

X1 = (1 + np.sin(B * 10.)) * A**(2.)

figure, axes = plt.subplots(2, 1)

pcm = axes[0].pcolormesh(A, B, X1,
						norm = colors.PowerNorm(gamma = 1./2.),
						cmap ='PuBu_r')

figure.colorbar(pcm, ax = axes[0],
				extend ='max')

pcm = axes[1].pcolormesh(A, B, X1,
						cmap ='PuBu_r')

figure.colorbar(pcm, ax = axes[1],
				extend ='max')

plt.show()
