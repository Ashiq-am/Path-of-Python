# Importing pandas and numpy libraries
import pandas as pd
import numpy as np

# Creating a dummy DataFrame of 12 numbers randomly
# ranging from 150-180 for height
df = pd.DataFrame({'Height': [150.4, 157.6, 170, 176, 164.2, 155,
							159.2, 175, 162.4, 176, 153, 170.9]})

# Printing DataFrame Before Sorting Continuous to Categories
print("Before: ")
print(df)

# A column of name 'Label' is created in DataFrame
# Categorizing Height into 3 Categories
# Short: (150,157], 150 is excluded & 157 is included
# Average: (157,169], 157 is excluded & 169 is included
# Tall: (169,180], 169 is excluded & 180 is included
df['Label'] = pd.cut(x=df['Height'],
					bins=[150, 157, 169, 180],
					labels=['Short', 'Average', 'Tall'])

# Printing DataFrame After Sorting Continuous to Categories
print("After: ")
print(df)

# Check the number of values in each bin
print("Categories: ")
print(df['Label'].value_counts())
