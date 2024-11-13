# Implementation of matplotlib function
import os
from matplotlib import font_manager as fm, rcParams
import matplotlib.pyplot as plt

fig, ax = plt.subplots()

fpath = os.path.join(rcParams["datapath"],
					"fonts / ttf / cmr10.ttf")
prop = fm.FontProperties(fname = fpath)
fname = os.path.split(fpath)[1]
ax.set_title('Title with special font: {}'.format(fname),
			fontproperties = prop, fontsize = 14)

w = ax.get_title()
ax.text(0.2, 0.6, "Previously assigned title : \n\n"+str(w),
		fontsize = 14)
ax.set_title("matplotlib.axes.Axes.get_title() function Example\n", fontweight ="bold")
plt.show()
