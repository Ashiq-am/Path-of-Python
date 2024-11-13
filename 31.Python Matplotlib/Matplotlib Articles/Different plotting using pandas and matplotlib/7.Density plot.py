# importing libraries
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

df = pd.DataFrame(np.random.rand(10, 5),
	columns =['A', 'B', 'C', 'D', 'E'])

ser = pd.Series(np.random.randn(1000))
ser.plot.kde()

plt.show()
