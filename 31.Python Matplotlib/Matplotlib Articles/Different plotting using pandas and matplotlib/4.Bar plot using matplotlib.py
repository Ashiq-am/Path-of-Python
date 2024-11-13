# importing libraries
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

ts = pd.Series(np.random.randn(1000), index = pd.date_range(
								'1/1/2000', periods = 1000))

df = pd.DataFrame(np.random.randn(1000, 4), index = ts.index,
									columns = list('ABCD'))

df3 = pd.DataFrame(np.random.randn(1000, 2),
			columns =['B', 'C']).cumsum()

df3['A'] = pd.Series(list(range(len(df))))
df3.iloc[5].plot.bar()
plt.axhline(0, color ='k')

plt.show()
