import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Creating sample data
dates = pd.date_range(start='2023-01-01', periods=100, freq='D')
data = np.random.randn(100).cumsum()
df = pd.DataFrame(data, index=dates, columns=['Value'])
# Plotting the time series
df.plot()
plt.xlabel('Date')
plt.ylabel('Value')
plt.title('Time Series Plot')
plt.show()
