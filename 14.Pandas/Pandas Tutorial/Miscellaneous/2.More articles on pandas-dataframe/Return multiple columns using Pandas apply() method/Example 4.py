# Program to illustrate the use of
# pandas.DataFrame.apply() method

# Importing required Libraries
import pandas
import numpy

# Creating dataframe
dataFrame = pandas.DataFrame([[4, 9], ] * 3, columns =['A', 'B'])
print('Data Frame:')
display(dataFrame)

# Using pandas.DataFrame.apply() on the data frame
print('Returning multiple columns from Pandas apply()')
dataFrame.apply(lambda x: [1, 2], axis = 1)
