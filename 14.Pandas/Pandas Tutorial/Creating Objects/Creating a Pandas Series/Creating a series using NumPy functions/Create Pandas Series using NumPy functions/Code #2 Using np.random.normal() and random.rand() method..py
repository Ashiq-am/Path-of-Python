# import pandas and numpy
import pandas as pd
import numpy as np

# series with numpy random.normal
ser3 = pd.Series(np.random.normal())
print(ser3)

# series with numpy random.normal
ser4 = pd.Series(np.random.normal(0.0, 1.0, 5))
print("\n", ser4)

# series with numpy random.rand
ser5 = pd.Series(np.random.rand(10))
print("\n", ser5)
