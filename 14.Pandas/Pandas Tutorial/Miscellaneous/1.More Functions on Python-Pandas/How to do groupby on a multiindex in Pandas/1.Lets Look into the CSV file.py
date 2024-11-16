# importing pandas library
# as alias pd
import pandas as pd

# storing the data in the df dataframe
# using pandas 'read_csv()'.
df = pd.read_csv('homelessness.csv')

print(df.head())
