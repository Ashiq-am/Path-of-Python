# importing libraries
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

df4 = pd.DataFrame({'a': np.random.randn(1000) + 1,
					'b': np.random.randn(1000),
					'c': np.random.randn(1000) - 1},
						columns =['a', 'b', 'c'])
plt.figure()

df4.plot.hist(alpha = 0.5)
plt.show()
