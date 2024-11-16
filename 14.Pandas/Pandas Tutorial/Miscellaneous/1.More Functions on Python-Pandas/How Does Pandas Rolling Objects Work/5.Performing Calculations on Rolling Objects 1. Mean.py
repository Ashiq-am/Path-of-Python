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

# calculationg rolling mean
rolling_mean = rolling_data.mean()
print(rolling_mean)
