# importing libraries
import pandas as pd
import numpy as np


num = {'Integers': [10, 15, 30, 40, 55, np.nan,
					75, np.nan, 90, 150, np.nan]}

# Create the dataframe
df = pd.DataFrame(num, columns=['Integers'])

# applying the method
count_nan = df['Integers'].isnull().sum()

# printing the number of values present
# in the column
print('Number of NaN values present: ' + str(count_nan))
