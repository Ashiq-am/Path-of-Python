import pandas as pd
data = {
    'Name': ['Alice', 'Bob', 'Charlie'],'Age': [25, 30, 35],'Score': [85, 90, 88]}
df = pd.DataFrame(data)

# 1. RangeIndex (Default)
print("1. RangeIndex (Default):")
print(df, "\n")

# 2. Int64Index
df.index = [101, 102, 103]
print("2. Int64Index:")
print(df, "\n")

# 3. Float64Index
df.index = [1.1, 2.2, 3.3]
print("3. Float64Index:")
print(df, "\n")

# 4. DatetimeIndex
df.index = pd.date_range(start='2024-01-01', periods=3, freq='D')
print("4. DatetimeIndex:")
print(df, "\n")

# 5. MultiIndex
df.index = pd.MultiIndex.from_tuples(
    [('Group1', 'A'), ('Group1', 'B'), ('Group2', 'A')],
    names=['Group', 'Subgroup']
)
print("5. MultiIndex:")
print(df, "\n")