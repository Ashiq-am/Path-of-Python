from pandas import np
from pandas.tests.extension.conftest import data

np.corrcoef(data,rowvar=False)
