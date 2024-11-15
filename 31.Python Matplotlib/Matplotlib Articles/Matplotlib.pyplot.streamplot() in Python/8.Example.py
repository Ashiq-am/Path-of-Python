import sys
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Circle

# Function to determin electric field
def E(q, r0, x, y):
	den = np.hypot(x-r0[0], y-r0[1])**3
	return q * (x - r0[0]) / den, q * (y - r0[1]) / den

# Grid of x, y points
nx, ny = 64, 64
x = np.linspace(-2, 2, nx)
y = np.linspace(-2, 2, ny)
X, Y = np.meshgrid(x, y)

# Create a multipole with nq charges of
# alternating sign, equally spaced
# on the unit circle.

# Increase the power with increase in charge
nq = 2**1
charges = []
for i in range(nq):
	q = i % 2 * 2 - 1
	charges.append((q, (np.cos(2 * np.pi * i / nq),
						np.sin(2 * np.pi * i / nq))))

# Electric field vector, E =(Ex, Ey)
# as separate components
Ex, Ey = np.zeros((ny, nx)), np.zeros((ny, nx))

for charge in charges:
	ex, ey = E(*charge, x = X, y = Y)
	Ex += ex
	Ey += ey

fig = plt.figure(figsize =(18, 8))
ax = fig.add_subplot(111)

# Plotting the streamlines with
# proper color and arrow
color = 2 * np.log(np.hypot(Ex, Ey))
ax.streamplot(x, y, Ex, Ey, color = color,
			linewidth = 1, cmap = plt.cm.inferno,
			density = 2, arrowstyle ='->',
			arrowsize = 1.5)

# Add filled circles for the charges
# themselves
charge_colors = {True: '#AA0000',
				False: '#0000AA'}

for q, pos in charges:
	ax.add_artist(Circle(pos, 0.05,
						color = charge_colors[q>0]))

ax.set_xlabel('X-axis')
ax.set_ylabel('X-axis')
ax.set_xlim(-2, 2)
ax.set_ylim(-2, 2)
ax.set_aspect('equal')

plt.show()
