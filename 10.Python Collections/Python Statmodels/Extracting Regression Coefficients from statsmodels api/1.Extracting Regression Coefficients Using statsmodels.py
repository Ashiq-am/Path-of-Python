import numpy as np
import pandas as pd

np.random.seed(0)
X = np.random.rand(100, 1)
y = 3 * X.squeeze() + 2 + np.random.randn(100) * 0.5

data = pd.DataFrame({'X': X.squeeze(), 'y': y})
