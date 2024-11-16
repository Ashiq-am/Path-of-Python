import calendar
import seaborn as sns
import pandas as pd

dataframe['Date'] = dataframe.index

# Splitting the Date into Year and Month
dataframe['Year'] = dataframe['Date'].dt.year
dataframe['Month'] = dataframe['Date'].dt.month

# Creating a Pivot Table with "A"
# column values and is Month indexed.
table_df = pd.pivot_table(dataframe, values=["A"],
								index=["Month"],
								columns=["Year"],
								fill_value=0,
								margins=True)

# Naming the index, can be generated
# using calendar.month_abbr[i]
mon_name = [['Jan', 'Feb', 'Mar', 'Apr',
			'May', 'Jun', 'Jul', 'Aug',
			'Sep','Oct', 'Nov', 'Dec', 'All']]

# Indexing using Month Names
table_df = table_df.set_index(mon_name)

# Creating a heatmap using sns with Red,
# Yellow & Green Colormap.
ax = sns.heatmap(table_df, cmap='RdYlGn_r',
				robust=True, fmt='.2f',
				annot=True, linewidths=.6,
				annot_kws={'size':10},
				cbar_kws={'shrink':.5,
						'label':'"A" values'})

# Setting the Tick Labels, Title and x & Y labels
ax.set_yticklabels(ax.get_yticklabels())
ax.set_xticklabels(ax.get_xticklabels())
plt.title('"A" Value Analysis', pad=14)
plt.xlabel('Year')
plt.ylabel('Months')
