import numpy
from matplotlib import pyplot as plt
from matplotlib import colors


# dummy data to plot
x = numpy.linspace(0, 2*numpy.pi, 30)
y = numpy.linspace(0, 2*numpy.pi, 20)
[A, B] = numpy.meshgrid(x, y)
Q = numpy.sin(A)*numpy.cos(B)

fig = plt.figure()
plt.ion()

# yellow to green to red
# colormap
plt.set_cmap('brg')

ax = fig.add_subplot(1, 2, 1)
plt.pcolor(A, B, Q)
plt.colorbar()

ax = fig.add_subplot(1, 2, 2)

# defining the scale, with white
# at zero
vmin = -0.2
vmax = 0.8
norms = colors.DivergingNorm(vmin=vmin,
							vcenter=0,
							vmax=vmax)

plt.pcolor(A, B, Q,
		vmin=vmin,
		vmax=vmax,
		norm=norms)

plt.colorbar()
