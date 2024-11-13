import matplotlib.pyplot as plt
from matplotlib.patches import Polygon

fig, ax = plt.subplots()
polygon = Polygon([(0.2, 0.2), (0.8, 0.2), (0.5, 0.8)], edgecolor='green', facecolor='lightgreen')
ax.add_patch(polygon)
ax.set_xlim(0, 1)
ax.set_ylim(0, 1)
ax.set_aspect('equal')
plt.grid(True)
plt.title('Polygon')
plt.show()
