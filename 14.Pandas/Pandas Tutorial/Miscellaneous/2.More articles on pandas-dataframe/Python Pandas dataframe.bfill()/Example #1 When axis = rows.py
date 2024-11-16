# Fill across the row
from pandas.tests.groupby.test_value_counts import df

df.bfill(axis ='rows')




"""

then value in current na cells are filled from the corresponding value 
in the next row. If the next row is also na value 
then it won’t be populated

"""
