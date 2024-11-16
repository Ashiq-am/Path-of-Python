# Importing pandas and numpy libraries
import pandas as pd
import numpy as np

# Creating a dummy DataFrame of 15 numbers randomly
# ranging from 1-100 for age
df = pd.DataFrame({'Age': [42, 15, 67, 55, 1, 29, 75, 89, 4,
						10, 15, 38, 22, 77]})

# Printing DataFrame Before sorting Continuous
# to Categories
print("Before: ")
print(df)

# A column of name 'Label' is created in DataFrame
# Categorizing Age into 4 Categories
# Baby/Toddler: (0,3], 0 is excluded & 3 is included
# Child: (3,17], 3 is excluded & 17 is included
# Adult: (17,63], 17 is excluded & 63 is included
# Elderly: (63,99], 63 is excluded & 99 is included
df['Label'] = pd.cut(x=df['Age'], bins=[0, 3, 17, 63, 99],
					labels=['Baby/Toddler', 'Child', 'Adult',
							'Elderly'])

# Printing DataFrame after sorting Continuous to
# Categories
print("After: ")
print(df)

# Check the number of values in each bin
print("Categories: ")
print(df['Label'].value_counts())
