import seaborn as sns
import pandas as pd
import numpy as np

# Generate sample time series data
date_range = pd.date_range(start='2020-01-01', periods=100, freq='D')
data = np.random.randn(100).cumsum()

# Create a DataFrame
df = pd.DataFrame(data, index=date_range, columns=['Value'])

# Plot the time series data using Seaborn
sns.set(style='darkgrid')
plt.figure(figsize=(10, 6))
sns.lineplot(x=df.index, y='Value', data=df)
plt.title('Time Series Data')
plt.xlabel('Date')
plt.ylabel('Value')
plt.show()
