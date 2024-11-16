# importing pandas library from
# python
import pandas as pd

# Creating an array of names
arrays = ['Sohom','Suresh','kumkum','subrata']

# Creating an array of ages
age= [10, 11, 12, 13]

# Creating an array of marks
marks=[90,92,23,64]

# Using MultiIndex.from_arrays, we are
# combining the arrays together along
# with their names and creating multi-index
# with each element from the 3 arrays into
# different rows
pd.MultiIndex.from_arrays([arrays,age,marks], names=('names', 'age','marks'))
