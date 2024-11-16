# Import library
import pandas as pd

# Reading csv file
df = pd.read_csv('StudentData.csv')

# Here filtering the rows according to
# Grade column which has notnull value.
df = df.loc[df['Grade'].notnull()]

# Displaying result
print(df)
