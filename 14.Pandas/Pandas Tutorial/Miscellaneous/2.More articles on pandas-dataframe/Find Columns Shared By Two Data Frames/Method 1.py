# Importing libraries
import pandas as pd
import numpy as np

# Creating Dataframes
a = [{'Name': 'abc', 'Age': 8, 'Grade': 3},{'Name': 'xyz', 'Age': 9, 'Grade': 3}]
df1 = pd.DataFrame(a)
b = [{'ID': 1,'Name': 'abc', 'Age': 8},{'ID': 2,'Name': 'xyz', 'Age': 9}]
df2 = pd.DataFrame(b)

# Pring Dataframes
display(df1)
display(df2)

# Finding Common columns
a = np.intersect1d(df2.columns, df1.columns)

# Printing common columns
print ("Common Columns:",a)
