import numpy as np
import matplotlib.pyplot as plt

Q = [(0, 0, 1)]

x1, y1 = -5, -5
x2, y2 = 5, 5
lres = 10
m, n = lres * (y2 - y1), lres * (x2 - x1)
x, y = np.linspace(x1, x2, n), np.linspace(y1, y2, m)
x, y = np.meshgrid(x, y)
Ex = np.zeros((m, n))
Ey = np.zeros((m, n))

k = 9 * 10 ** 9
for j in range(m):
    for i in range(n):
        xp, yp = x[j][i], y[j][i]
        for q in Q:
            deltaX = xp - q[0]
            deltaY = yp - q[1]

            distance = (deltaX ** 2 + deltaY ** 2) ** 0.5

            E = (k * q[2]) / (distance ** 2)
            Ex[j][i] += E * (deltaX / distance)
            Ey[j][i] += E * (deltaY / distance)

fig, ax = plt.subplots()
ax.set_aspect('equal')
ax.scatter([q[0] for q in Q], [q[1] for q in Q], c='red', s=[abs(q[2]) * 50 for q in Q], zorder=1)
for q in Q: ax.text(q[0] + 0.1, q[1] - 0.3, '{} unit'.format(q[2]), color='black', zorder=2)
ax.streamplot(x, y, Ex, Ey, linewidth=1, density=1.5, zorder=0)

plt.title('Electrostatic Field Simulation')
plt.show()
