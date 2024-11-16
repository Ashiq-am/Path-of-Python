import pandas as pd

data1 = {
    'A': [1, 2, 3, 4],
    'B': ['a', 'b', 'c', 'd'],
    'C': [10, 20, 30, 40]
}
df1 = pd.DataFrame(data1)

data2 = {
    'A': [3, 4, 5, 6],
    'B': ['c', 'd', 'e', 'f'],
    'D': [300, 400, 500, 600]
}
df2 = pd.DataFrame(data2)

print("DataFrame 1:")
print(df1)
print("\nDataFrame 2:")
print(df2)
