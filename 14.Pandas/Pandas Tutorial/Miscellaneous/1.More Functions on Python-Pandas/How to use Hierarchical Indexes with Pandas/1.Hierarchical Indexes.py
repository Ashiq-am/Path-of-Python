# importing pandas library as alias pd
import pandas as pd

# calling the pandas read_csv() function.
# and storing the result in DataFrame df
df = pd.read_csv('homelessness.csv')

print(df.head())
