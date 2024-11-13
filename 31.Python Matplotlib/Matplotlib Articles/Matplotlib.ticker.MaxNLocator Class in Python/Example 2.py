import matplotlib.pyplot as plt
from matplotlib.ticker import MaxNLocator, IndexFormatter


ax = df.plot()

ax.xaxis.set_major_locator(MaxNLocator(11))
ax.xaxis.set_major_formatter(IndexFormatter(df.index))

ax.grid(which ='minor', alpha = 0.2)
ax.grid(which ='major', alpha = 0.5)

ax.legend().set_visible(False)
plt.xticks(rotation = 75)
plt.tight_layout()

plt.show()
