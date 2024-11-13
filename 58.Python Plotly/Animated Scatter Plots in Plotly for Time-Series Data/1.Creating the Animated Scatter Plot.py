import pandas as pd
import numpy as np

# Set the random seed for reproducibility
np.random.seed(42)

# Create a date range
date_range = pd.date_range(start='2022-01-01', end='2023-12-01', freq='MS')

# Create a synthetic dataset
data = {
    'date': date_range,
    'sales': np.random.randint(100, 1000, size=len(date_range)),
    'profit': np.random.randint(10, 300, size=len(date_range)),  # New profit column
    'category': np.random.choice(['A', 'B', 'C'], size=len(date_range))
}

df = pd.DataFrame(data)

# Display the first few rows of the dataset
print(df.head())
