import pandas as pd
import numpy as np

# Generate sample time series data
date_range = pd.date_range(start='2020-01-01', periods=100, freq='D')
data = np.random.randn(100).cumsum()

# Create a DataFrame
df = pd.DataFrame(data, index=date_range, columns=['Value'])

# Plot the time series data using Pandas
df.plot(figsize=(10, 6), title='Time Series Data', grid=True)
plt.xlabel('Date')
plt.ylabel('Value')
plt.show()
