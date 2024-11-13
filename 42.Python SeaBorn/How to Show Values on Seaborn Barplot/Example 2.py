# import the necessary python packages
import pandas as pd
import seaborn as sns
import numpy as np

# read the dataset using pandas read_csv
# function
data = pd.read_csv(r"path to\tips.csv")

# group the multi level categorical variables
# and reset_ the index to flatten the index
groupedvalues = data.groupby('day').sum().reset_index()

# use sns barplot to plot bar plot
# between days and tip value
ax = sns.barplot(x='day', y='tip',
				data=groupedvalues,
				errwidth=0)

# now simply assign the bar values to
# each bar by passing containers method
# to bar_label function
ax.bar_label(ax.containers[0])
