# combining series and dataframe
from turtle import pd

from pandas.tests.test_downstream import df

res = pd.concat([df, s1], axis=1)

res