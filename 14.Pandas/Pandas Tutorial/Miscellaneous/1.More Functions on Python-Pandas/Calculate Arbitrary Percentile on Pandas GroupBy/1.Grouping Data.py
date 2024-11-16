# import pandas module
import pandas as pd

# Sample dataset
data = {
    'Category': ['A', 'A', 'A', 'B', 'B', 'B', 'C', 'C', 'C'],
    'Value': [10, 20, 30, 40, 50, 60, 70, 80, 90]
}

# create dataframe
df = pd.DataFrame(data)

# group data using groupby() on Category
grouped = df.groupby('Category').sum()

print(grouped)
