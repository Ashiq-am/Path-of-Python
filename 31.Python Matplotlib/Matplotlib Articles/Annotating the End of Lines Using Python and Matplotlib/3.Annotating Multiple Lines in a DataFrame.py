import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

rows = 75
df = pd.DataFrame(np.random.randint(-5, 5, size=(rows, 3)), columns=['A', 'B', 'C'])
df = df.cumsum()
ax = df.plot()

# Annotate the end of each line
for line, name in zip(ax.lines, df.columns):
    y = line.get_ydata()[-1]
    ax.annotate(name, xy=(1, y), xytext=(6, 0), color=line.get_color(), xycoords=ax.get_yaxis_transform(), textcoords="offset points", size=14, va="center")

plt.legend(loc='lower left')
plt.show()
