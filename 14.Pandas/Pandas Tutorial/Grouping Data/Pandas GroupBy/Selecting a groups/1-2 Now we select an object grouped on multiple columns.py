# selecting object grouped
# on multiple columns
from pandas.tests.groupby.test_value_counts import df

grp = df.groupby(['Name', 'Qualification'])
grp.get_group(('Jai', 'Msc'))
