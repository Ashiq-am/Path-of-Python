import pandas as pd
import numpy as np

# Create a DataFrame with duplicate records
data = {
    'ID': [1, 2, 3, 4, 5, 1, 6, 2, 7],
    'Name': ['John', 'Alice', 'Bob', 'Charlie', 'Emma', 'John', 'Eva', 'Alice', 'David'],
    'Age': [25, 30, 35, 40, 45, 25, 50, 30, 55]
}

df = pd.DataFrame(data)
print(df)
