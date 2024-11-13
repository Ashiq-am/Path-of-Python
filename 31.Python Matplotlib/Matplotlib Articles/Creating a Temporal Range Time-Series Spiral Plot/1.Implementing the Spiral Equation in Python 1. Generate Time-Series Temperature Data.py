import pandas as pd
import numpy as np

date_range = pd.date_range(start="2023-01-01", end="2023-12-31", freq='D')

# Generate random temperature data
np.random.seed(42)  # For reproducibility
temperature_data = np.random.uniform(low=-10, high=35, size=len(date_range))

# Create a DataFrame with the generated data
df = pd.DataFrame({
    'date': date_range,
    'temperature': temperature_data
})

print(df.head())
