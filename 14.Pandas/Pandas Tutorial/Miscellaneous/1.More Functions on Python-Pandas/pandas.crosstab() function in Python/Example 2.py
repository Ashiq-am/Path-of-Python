# importing package
import pandas

# create some data
foo = pandas.Categorical(['a', 'b'],
						categories=['a', 'b', 'c'])

bar = pandas.Categorical(['d', 'e'],
						categories=['d', 'e', 'f'])

# form crosstab with dropna=True (default)
pandas.crosstab(foo, bar)

# form crosstab with dropna=False
pandas.crosstab(foo, bar, dropna=False)
