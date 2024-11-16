# importing libraries
import pandas as pd
import numpy as np


num = {'Integers': [10, 15, 30, 40, 55, np.nan,
					75, np.nan, 90, 150, np.nan]}

# Create the dataframe
df = pd.DataFrame(num, columns=['Integers'])

# Applying the method
check_nan = df['Integers'].isnull().values.any()

# printing the result
print(check_nan)
