# code
import pandas as pd

# importing our dataset
df = pd.read_csv('hiring.csv')
# viewing the dataFrame
print(df)

# we change the case of all the strings
# in experience column to uppercase
df['experience'] = df['experience'].apply(str.upper)

# viewing the modified column
print(df['experience'])
