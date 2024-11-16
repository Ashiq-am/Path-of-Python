# importing pandas as pd
import pandas as pd

# creating a dictionary of integers
dict = {'Integers' : [10, 50, 100, 350, 700]}

# creating dataframe from dictionary
df = pd.DataFrame.from_dict(dict)
print(df)
print(df.dtypes)

print('\n')

# converting each value of column to a string
df['Integers'] = df['Integers'].map(str)
print(df)
print(df.dtypes)
