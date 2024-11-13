# import modules
import matplotlib.path as mpath
import matplotlib.patches as mpatches
import matplotlib.pyplot as plt

# adjust figure and assign coordinates
fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)

pp1 = plt.Rectangle((0.2, 0.75),
					0.4, 0.15)

pp2 = plt.Circle((0.7, 0.2), 0.15)

pp3 = plt.Polygon([[0.15, 0.15],
				[0.35, 0.4],
				[0.2, 0.6]])

# depict illustrations
ax.add_patch(pp1)
ax.add_patch(pp2)
ax.add_patch(pp3)
