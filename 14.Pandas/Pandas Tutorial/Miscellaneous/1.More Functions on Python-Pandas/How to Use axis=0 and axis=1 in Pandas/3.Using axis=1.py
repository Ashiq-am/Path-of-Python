# importing packages
import pandas as pd

# importing our dataset
df = pd.read_csv('hiring.csv')

# dropping the column named 'experience'
df = df.drop(['experience'], axis=1)

# 'viewing the dataframe
df.head()
