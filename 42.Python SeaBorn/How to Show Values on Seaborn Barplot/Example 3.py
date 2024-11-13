# import the necessary python packages
import pandas as pd
import seaborn as sns
import numpy as np

# read the dataset using pandas read_csv
# function
data = pd.read_csv(r"path to\tips.csv")

# group the multilevel categorical
# values and flatten the index
groupedvalues = data.groupby('day').sum().reset_index()

# define the color palette of different colors
pal = sns.color_palette("Greens_d", len(groupedvalues))
# use argsort method
rank = groupedvalues["total_bill"].argsort()

# use dataframe grouped by days to plot a
# bar chart between days and total bill
ax = sns.barplot(x='day', y='total_bill',
				data=groupedvalues,
				palette=np.array(pal[::-1])[rank])

# now use a for loop to iterate through
# each row of the grouped dataframe
# assing bar value to each row
for index, row in groupedvalues.iterrows():
	ax.text(row.name, row.tip, round(row.total_bill, 2),
			color='white', ha='center')
