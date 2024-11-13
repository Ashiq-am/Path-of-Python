import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

dates = pd.date_range(start="2023-01-01", end="2023-12-31", freq="D")
data = np.random.randn(len(dates))

df = pd.DataFrame(data, index=dates, columns=["Value"])
df.plot()
plt.show()
