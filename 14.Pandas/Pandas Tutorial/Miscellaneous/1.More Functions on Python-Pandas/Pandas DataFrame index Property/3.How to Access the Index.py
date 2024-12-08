import pandas as pd
data = {'Product': ['Laptop', 'Smartphone', 'Tablet'],'Price': [1000, 800, 400],'Stock': [10, 20, 15]}
df = pd.DataFrame(data)

# Setting a custom index with a name
df.index = ['P001', 'P002', 'P003']
df.index.name = 'ProductID'

# Accessing the index
print("Index:")
print(df.index)

# Accessing the name of the index
print("\nIndex Name:")
print(df.index.name)

# Accessing the values of the index
print("\nIndex Values:")
print(df.index.values)