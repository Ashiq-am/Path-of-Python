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

# calculationg rolling standard deviation
rolling_std = rolling_data.std()
print(rolling_std)
