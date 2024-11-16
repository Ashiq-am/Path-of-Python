import matplotlib.pyplot as plt
from pandas.tests.reshape.merge.test_merge_index_as_string import df1

plt.style.use('ggplot')
df1['A'].hist()
