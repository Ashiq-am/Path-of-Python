# code
import pandas as pd

# Example DataFrame
data = {'A': [1, 2, np.nan, 4], 'B': [5, np.nan, 7, 8]}
df = pd.DataFrame(data)

# Check for NaN values
nan_check_df = df.isnull()
print(nan_check_df)
