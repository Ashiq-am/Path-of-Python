# selecting a single group
from pandas.tests.groupby.test_value_counts import df

grp = df.groupby('Name')
grp.get_group('Jai')
