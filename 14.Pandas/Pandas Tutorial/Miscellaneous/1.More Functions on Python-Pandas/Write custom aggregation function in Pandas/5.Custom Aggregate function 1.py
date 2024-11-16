# Importing reduce for
# rolling computations
from functools import reduce

# define a Custom aggregation
# function for finding total
def total(series):
	return reduce(lambda x, y: x + y, series)

# Grouping the output according to
# student id and printing the corresponding
# total marks and to check whether the
# output is correct or not, sum function
# is also used to print the sum.
df.groupby('stud_id').agg({'marks': ['sum', total]})
