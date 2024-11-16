import pandas as pd

data = {'A': [1, 2, 3, 4, 5], 'B': [10, 20, 30, 40, 50]}
df = pd.DataFrame(data)
print("Before Replacing:\n", df)

df.replace({2: 200, 4: 400}, inplace=True)
print("After Replacing:\n", df)
