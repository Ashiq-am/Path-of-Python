import pandas as pd

# define data
from IPython.core.display import display

data = {'A': [1, 2, 3], 'B': [4, 5, 6], 'C': [7, 8, 9]}

# create dataframe
df = pd.DataFrame(data)

print("Original DataFrame:")
display(df)

# shift column 'C' to first position
first_column = df.pop('C')

# insert column using insert(position,column_name,first_column) function
df.insert(0, 'C', first_column)

print()
print("Final DataFrame")
display(df)
