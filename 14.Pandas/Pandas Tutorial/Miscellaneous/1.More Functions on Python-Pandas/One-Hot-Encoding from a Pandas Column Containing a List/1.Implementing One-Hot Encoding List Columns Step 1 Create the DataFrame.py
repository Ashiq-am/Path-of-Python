import pandas as pd

data = {
    'ID': [1, 2, 3],
    'Categories': [['A', 'B'], ['B', 'C'], ['A', 'C', 'D']]
}

df = pd.DataFrame(data)
print(df)
