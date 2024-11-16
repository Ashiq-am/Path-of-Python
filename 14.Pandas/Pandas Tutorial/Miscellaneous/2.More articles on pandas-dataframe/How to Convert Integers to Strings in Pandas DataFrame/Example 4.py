# importing pandas as pd
import pandas as pd

# creating a dictionary of integers
dict = {'Roll No.' : [1, 2, 3, 4, 5], 'Marks':[79, 85, 91, 81, 95]}

# creating dataframe from dictionary
df = pd.DataFrame.from_dict(dict)
print(df)
print(df.dtypes)

print('\n')

# converting each value of column to a string
df = df.applymap(str)
print(df)
print(df.dtypes)
