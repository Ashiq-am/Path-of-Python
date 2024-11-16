import numpy as np

# Creating a DataFrame
data = {'A': [10, 20, 30], 'B': [5, 15, 25]}
df = pd.DataFrame(data)

# Introducing missing values
series_with_nan = pd.Series([1, 2, np.nan, 4])

# Filling missing values with 0
filled_series = series_with_nan.fillna(0)
print("Filled Series:\n", filled_series)
