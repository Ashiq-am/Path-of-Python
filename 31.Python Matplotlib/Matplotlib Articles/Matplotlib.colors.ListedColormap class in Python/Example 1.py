import matplotlib.pyplot as plt
import numpy as np
import matplotlib.colors

a = np.linspace(-3, 3)
A, B = np.meshgrid(a, a)
X = np.exp(-(A**2 + B**2))
figure, (axes1, axes2) = plt.subplots(ncols = 2)

colors =["green", "orange",
		"gold", "blue", "k",
		"#550011", "purple",
		"red"]

axes1.set_title(" color list")
contour = axes1.contourf(A, B, X,
						colors = colors)

axes2.set_title("with colormap")
cmap = matplotlib.colors.ListedColormap(colors)
contour = axes2.contourf(A, B, X, cmap = cmap)
figure.colorbar(contour)

plt.show()
