import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import ticker

data = [
	('Area 1', 'Bar 1', 2, 2),
	('Area 2', 'Bar 2', 1, 3),
	('Area 1', 'Bar 3', 3, 2),
	('Area 2', 'Bar 4', 2, 3),
]

df = pd.DataFrame(data, columns =('A', 'B',
								'D1', 'D2'))

df = df.set_index(['A', 'B'])
df.sort_index(inplace = True)

# Remove the index names for the plot,
# or it'll be used as the axis label
df.index.names = ['', '']

ax = df.plot(kind ='barh', stacked = True)

minor_locator = ticker.AutoMinorLocator(2)

ax.yaxis.set_minor_locator(minor_locator)

ax.set_yticklabels(df.index.get_level_values(1))
ax.set_yticklabels(df.index.get_level_values(0).unique(),
				minor = True)

ax.set_yticks(np.arange(0.5, len(df), 2),
			minor = True)

ax.tick_params(axis ='y', which ='minor',
			direction ='out', pad = 50)

plt.show()
