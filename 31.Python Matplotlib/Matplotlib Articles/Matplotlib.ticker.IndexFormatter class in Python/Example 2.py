from matplotlib.ticker import IndexFormatter, IndexLocator
import pandas as pd
import matplotlib.pyplot as plt


years = range(2015, 2018)
fields = range(4)
days = range(4)
bands = ['R', 'G', 'B']

index = pd.MultiIndex.from_product(
	[years, fields], names =['year', 'field'])

columns = pd.MultiIndex.from_product(
	[days, bands], names =['day', 'band'])

df = pd.DataFrame(0, index = index, columns = columns)

df.loc[(2015, ), (0, )] = 1
df.loc[(2016, ), (1, )] = 1
df.loc[(2017, ), (2, )] = 1
ax = plt.gca()
plt.spy(df)

xbase = len(bands)
xoffset = xbase / 2
xlabels = df.columns.get_level_values('day')

ax.xaxis.set_major_locator(IndexLocator(base = xbase,
										offset = xoffset))

ax.xaxis.set_major_formatter(IndexFormatter(xlabels))

plt.xlabel('Day')
ax.xaxis.tick_bottom()

ybase = len(fields)
yoffset = ybase / 2
ylabels = df.index.get_level_values('year')

ax.yaxis.set_major_locator(IndexLocator(base = ybase,
										offset = yoffset))

ax.yaxis.set_major_formatter(IndexFormatter(ylabels))

plt.ylabel('Year')

plt.show()
