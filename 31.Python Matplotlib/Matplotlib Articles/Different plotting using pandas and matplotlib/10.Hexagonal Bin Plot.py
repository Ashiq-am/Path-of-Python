# importing libraries
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

df = pd.DataFrame(np.random.randn(1000, 2), columns =['a', 'b'])

df['a'] = df['a'] + np.arange(1000)
df.plot.hexbin(x ='a', y ='b', gridsize = 25)
plt.show()
