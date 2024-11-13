# Computing geometric mean
# Storing into a DataFrame column
from pandas.tests.groupby.test_value_counts import df
from scipy.stats import stats

df['Geometric Mean'] = stats.gmean(df.iloc[:, 1:3], axis=1)
df
