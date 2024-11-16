# We want NaN values in dataframe.
# so let's fill the last row with NaN value
from pandas import np
from pandas.tests.groupby.test_value_counts import df

df.iloc[-1] = np.nan

df
