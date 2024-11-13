# importing libraries
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

df = pd.DataFrame(np.random.rand(500, 4),
		columns =['a', 'b', 'c', 'd'])

df.plot.scatter(x ='a', y ='b')
plt.show()
