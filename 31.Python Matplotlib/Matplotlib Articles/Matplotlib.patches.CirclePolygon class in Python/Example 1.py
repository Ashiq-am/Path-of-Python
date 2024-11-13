import matplotlib.pyplot as plt
from matplotlib.patches import CirclePolygon


circle = CirclePolygon((0, 0),
					radius = 0.75,
					fc = 'y')

plt.gca().add_patch(circle)

verts = circle.get_path().vertices
trans = circle.get_patch_transform()
points = trans.transform(verts)

plt.plot(points[:, 0], points[:, 1])
plt.axis('scaled')

plt.show()
