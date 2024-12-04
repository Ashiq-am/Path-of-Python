import numpy as np
import pandas as pd

array = np.array([10, 20, 30, 40, 50])
df = pd.DataFrame(array, columns=['Values'])
print(df)