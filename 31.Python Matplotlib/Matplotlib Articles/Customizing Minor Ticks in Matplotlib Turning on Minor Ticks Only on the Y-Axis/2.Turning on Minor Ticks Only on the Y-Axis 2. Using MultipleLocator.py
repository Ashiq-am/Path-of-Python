import matplotlib.pyplot as plt
import matplotlib.ticker as tck

fig, ax = plt.subplots()
plt.plot([0, 2, 4], [3, 6, 1])
ax.yaxis.set_minor_locator(tck.AutoMinorLocator())
plt.show()
