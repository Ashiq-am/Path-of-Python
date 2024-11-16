import pandas as pd

# reading a csv file
from IPython.core.display import display

df1 = pd.read_csv("data1.csv")

# change 2nd column name with index number
df1.columns.values[2] = "city"

# Display DataFrame
display(df1)
