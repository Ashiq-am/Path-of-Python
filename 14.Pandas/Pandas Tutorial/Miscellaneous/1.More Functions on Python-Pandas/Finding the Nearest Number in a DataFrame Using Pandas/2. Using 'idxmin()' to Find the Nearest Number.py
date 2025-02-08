import pandas as pd
import numpy as np

df = pd.DataFrame({
    'values': [10, 20, 30, 40, 50]
})

# Target number
target = 33


differences = np.abs(df['values'] - target)
nearest_index = differences.idxmin()

nearest_value = df['values'].iloc[nearest_index]
print(f"Nearest value to {target} is {nearest_value}")