import pandas as pd
import numpy as np

df = pd.DataFrame({
    'values': [10, 20, 30, 40, 50]
})

# Target number
target = 33
N = 3 # Number of nearest values you want


differences = np.abs(df['values'] - target)
nearest_indices = differences.argsort()[:N]

nearest_values = df['values'].iloc[nearest_indices]
print(f"The {N} nearest values to {target} are {nearest_values.tolist()}")