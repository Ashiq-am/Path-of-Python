import pandas as pd

data = {'A': [1, 2, 3]}
df = pd.DataFrame(data)
print("Before Replacing:\n", df)

df['A'] = df['A'].map({1: 'one', 2: 'two', 3: 'three'})
print("After Replacing:\n", df)
