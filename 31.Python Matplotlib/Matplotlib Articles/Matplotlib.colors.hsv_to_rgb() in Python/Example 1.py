import matplotlib.pyplot as plt
import matplotlib.colors
import numpy as np


# helper function to find
# mid-points
def helper(z):
    k = ()
    for i in range(z.ndim):
        z = (z[k + np.index_exp[:-1]] + z[k + np.index_exp[1:]]) / 2.0
        k += np.index_exp[:]

    return z


# dummy coordinates with rgb
# values attached with each
s, alpha, x = np.mgrid[0:1:11j,
              0:np.pi * 2:25j,
              -0.5:0.5:11j]
a = s * np.cos(alpha)
b = s * np.sin(alpha)

sc, alphac, xc = helper(s), helper(alpha), helper(x)

# wobbly torus about [0.7, *, 0]
sphere = (sc - 0.7) ** 2 + (xc + 0.2 * np.cos(alphac * 2)) ** 2 < 0.2 ** 2

# combining the color components
hsv = np.zeros(sphere.shape + (3,))
hsv[..., 0] = alphac / (np.pi * 2)
hsv[..., 1] = sc
hsv[..., 2] = xc + 0.5

# the hsv to rgb function
plot_colors = matplotlib.colors.hsv_to_rgb(hsv)

# and plot everything
figure = plt.figure()
axes = figure.gca(projection='3d')

axes.voxels(a, b, x, sphere,
            facecolors=plot_colors,
            edgecolors=np.clip(2 * plot_colors - 0.5, 0, 1),
            linewidth=0.5)

plt.show()
