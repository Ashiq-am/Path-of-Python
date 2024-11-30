import pandas as pd

df1 = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]}, index=['a', 'b', 'c'])
df2 = pd.DataFrame({'C': [7, 8, 9], 'D': [10, 11, 12]}, index=['a', 'b', 'c'])
df3 = pd.DataFrame({'E': [13, 14, 15], 'F': [16, 17, 18]}, index=['a', 'b', 'c'])

# Join all three DataFrames based on their indices
result = df1.join([df2, df3])
print(result)