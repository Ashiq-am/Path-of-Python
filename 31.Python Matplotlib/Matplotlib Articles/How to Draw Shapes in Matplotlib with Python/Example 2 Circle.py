import matplotlib.pyplot as plt
from matplotlib.patches import Circle

fig, ax = plt.subplots()
circle = Circle((0.5, 0.5), radius=0.2, edgecolor='red', facecolor='lightcoral')
ax.add_patch(circle)
ax.set_xlim(0, 1)
ax.set_ylim(0, 1)
ax.set_aspect('equal')
plt.grid(True)
plt.title('Circle')
plt.show()
