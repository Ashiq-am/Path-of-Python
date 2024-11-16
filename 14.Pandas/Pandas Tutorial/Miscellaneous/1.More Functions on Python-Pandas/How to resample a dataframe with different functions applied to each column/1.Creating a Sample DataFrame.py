import pandas as pd
import numpy as np

# Create a date range
date_rng = pd.date_range(start='2024-01-01', end='2024-01-10', freq='D')

# Create a DataFrame
df = pd.DataFrame(date_rng, columns=['date'])
df.set_index('date', inplace=True)

# Add some random data
df['value1'] = np.random.randint(1, 100, size=(len(date_rng)))
df['value2'] = np.random.rand(len(date_rng)) * 100
df['value3'] = np.random.choice(['A', 'B', 'C'], size=(len(date_rng)))

print(df)
