import matplotlib.pyplot as plt
import numpy as np

t = np.arange(0.01, 5.0, 0.01)
s = np.exp(-t)

plt.plot(t, s)
plt.ylim(1, 0)
plt.ylabel('Display Y-axis Label', fontweight='bold')
plt.grid(True)

w = plt.get_figlabels()

plt.text(1.5, 0.58,
         "List of existing figure labels : \n"
         + str(w),
         fontsize=12)

plt.title('matplotlib.pyplot.get_figlabels() function\
Example', fontweight="bold")

plt.show()
