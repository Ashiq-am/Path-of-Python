import numpy as np
import matplotlib.pyplot as plt

start_point = 'lower'

diff = 0.025

a = b = np.arange(-3.0, 3.01, diff)
A, B = np.meshgrid(a, b)
X1 = np.exp(-A ** 2 - B ** 2)
X2 = np.exp(-(A - 1) ** 2 - (B - 1) ** 2)
X = (X1 - X2) * 2

RR, RC = X.shape

# putting NaNs in one corner:
X[-RR // 6:, -RC // 6:] = np.nan

X = np.ma.array(X)
# masking the other corner:
X[:RR // 6, :RC // 6] = np.ma.masked

# masking a circle in the middle:
INNER = np.sqrt(A ** 2 + B ** 2) < 0.5
X[INNER] = np.ma.masked

# using automatic selection of
# contour levels;
figure1, axes2 = plt.subplots(constrained_layout=True)
C = axes2.contourf(A, B, X, 10,
                   cmap=plt.cm.bone,
                   origin=start_point)

C2 = axes2.contour(C, levels=C.levels[::2],
                   colors='r', origin=start_point)

axes2.set_title('3 masked regions')
axes2.set_xlabel('length of word anomaly')
axes2.set_ylabel('length of sentence anomaly')

# Make a colorbar for the ContourSet
# returned by the contourf call.
cbar = figure1.colorbar(C)

cbar.ax.set_ylabel('coefficient of verbosity')

# Add the contour line levels
# to the colorbar
cbar.add_lines(C2)

figure2, axes2 = plt.subplots(constrained_layout=True)

# making a contour plot with the
# levels specified,
levels = [-1.5, -1, -0.5, 0, 0.5, 1]
C3 = axes2.contourf(A, B, X, levels,
                    colors=('r', 'g', 'b'),
                    origin=start_point,
                    extend='both')

# data below the lowest contour
# level yellow, data below the
# highest level green:
C3.cmap.set_under('yellow')
C3.cmap.set_over('green')

C4 = axes2.contour(A, B, X, levels,
                   colors=('k',),
                   linewidths=(3,),
                   origin=start_point)

axes2.set_title('Listed colors (3 masked regions)')

axes2.clabel(C4, fmt='% 2.1f',
             colors='w',
             fontsize=14)

figure2.colorbar(C3)

# Illustrating all 4 possible
# "extend" settings:
extends = ["neither", "both", "min", "max"]
cmap = plt.cm.get_cmap("winter")
cmap.set_under("green")
cmap.set_over("red")

figure, axes = plt.subplots(2, 2,
                            constrained_layout=True)

for ax, extend in zip(axes.ravel(), extends):
    cs = ax.contourf(A, B, X, levels,
                     cmap=cmap,
                     extend=extend,
                     origin=start_point)

    figure.colorbar(cs, ax=ax, shrink=0.9)
    ax.set_title("extend = % s" % extend)
    ax.locator_params(nbins=4)

plt.show()
