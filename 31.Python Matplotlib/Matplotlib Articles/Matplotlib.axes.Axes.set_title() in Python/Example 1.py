# Implementation of matplotlib function
import os
from matplotlib import font_manager as fm, rcParams
import matplotlib.pyplot as plt

fig, ax = plt.subplots()

fpath = os.path.join(rcParams["datapath"],
					"fonts/ttf/cmr10.ttf")

prop = fm.FontProperties(fname = fpath)
fname = os.path.split(fpath)[1]
ax.set_title('Title with special font: {}'.format(fname),
			fontproperties = prop,
			fontsize = 14)

plt.show()
