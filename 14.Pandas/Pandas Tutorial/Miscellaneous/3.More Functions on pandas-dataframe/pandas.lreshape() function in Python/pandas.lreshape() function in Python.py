# importing package
from turtle import pd

import numpy
import pandas

# create and view data
data = pandas.DataFrame({
	'hr1': [514, 573],
	'hr2': [545, 526],
	'team': ['Red Sox', 'Yankees'],
	'year1': [2007, 2007],
	'year2': [2008, 2008]
})
print(data)

# use pandas.lreshape() method
print(pd.lreshape(data, {'year': ['year1', 'year2'],'hr': ['hr1', 'hr2']}))
