# import module
from matplotlib.patches import PathPatch
from matplotlib.path import Path
import matplotlib.pyplot as plt
import numpy as np

# assign coordinates
coord = [(0, 20), (20, 20), (20, 20),
		(20, 20), (10, 10), (10, 10),
		(5, 5), (15, 5), (0, 0)]

instn = [Path.MOVETO, Path.LINETO, Path.LINETO,
		Path.LINETO, Path.CLOSEPOLY, Path.MOVETO,
		Path.LINETO, Path.LINETO, Path.CLOSEPOLY]

# adjust figure
coord = np.array(coord, float)
path = Path(coord, instn)
pathpatch = PathPatch(path)
fig, ax = plt.subplots()
ax.add_patch(pathpatch)

# depict illustration
ax.autoscale_view()
plt.show()
