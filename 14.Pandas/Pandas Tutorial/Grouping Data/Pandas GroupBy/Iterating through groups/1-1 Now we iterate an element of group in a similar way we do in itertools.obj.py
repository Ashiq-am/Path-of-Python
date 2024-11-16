# iterating an element
# of group
from pandas.tests.groupby.test_value_counts import df

grp = df.groupby('Name')
for name, group in grp:
	print(name)
	print(group)
	print()
