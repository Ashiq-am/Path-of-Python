import pandas as pd
import numpy as np

# Simulating DataFrame with random data
np.random.seed(42)
df = pd.DataFrame({'Numeric_Column': np.random.randint(1, 100, 5)})

# Displaying the original DataFrame
print("Original DataFrame:")
print(df)
