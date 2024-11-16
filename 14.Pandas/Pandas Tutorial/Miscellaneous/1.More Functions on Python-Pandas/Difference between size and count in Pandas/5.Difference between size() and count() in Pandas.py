import pandas as pd

data = {'A': [1, 2, 3, None, 5],
		'B': [6, 7, 8, 9, 10]}

df = pd.DataFrame(data)

# Calculates the total number of elements in the DataFrame
total_size = df.size
# Output: 10 (5 elements in column 'A' + 5 elements in column 'B')
print(total_size)

# Counts non-null values in column 'A'
count_column_A = df['A'].count()
# Output: 4 (4 non-null values in column 'A')
print(count_column_A)
