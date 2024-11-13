# import the necessary python packages
import pandas as pd
import numpy as np
import seaborn as sns

# create wide-form data
data = pd.DataFrame({'Summer': [17, 18, 19, 21, 27],
					'Winter': [33, 37, 33, 36, 12],
					'Spring': [14, 15, 16, 21, 22]})
# print the data
print(data)
# use melt to convert wide form to long form data
# use seaborn plot and specify the x and y columns
# and specify the dataframe
sns.boxplot(x='variable', y='value', data=pd.melt(data)).set(
	xlabel='Season',
	ylabel='Rainfall amount')
