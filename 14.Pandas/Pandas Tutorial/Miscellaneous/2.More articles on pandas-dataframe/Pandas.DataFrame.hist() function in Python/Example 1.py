# Importing pandas library
import pandas as pd

# Creating a Data frame
values = pd.DataFrame({
	'Length': [2.7, 8.7, 3.4, 2.4, 1.9],
	'Breadth': [4.24, 2.67, 7.6, 7.1, 4.9]
})

# Creating Histograms of columns 'Length'
# and 'Breadth' using Dataframe.hist()
# function
hist = values.hist(bins=5)
