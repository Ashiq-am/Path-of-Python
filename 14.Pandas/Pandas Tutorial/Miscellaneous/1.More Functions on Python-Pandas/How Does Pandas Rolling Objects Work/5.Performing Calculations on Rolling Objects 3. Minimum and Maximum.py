import pandas as pd
import numpy as np

# creating sample dataframe
data = pd.DataFrame({
    'value': np.random.randn(10)
})

# defining rolling window
window_size = 5

# creating rolling object
rolling_data = data['value'].rolling(window=window_size)

# calculationg rolling minimum and maximum
rolling_min = rolling_data.min()
rolling_max = rolling_data.max()
print(rolling_min)
print(rolling_max)
