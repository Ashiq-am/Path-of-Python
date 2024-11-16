import pandas as pd

# Define the size of the dataset
num_rows = 1000000  # 1 million rows

# Example DataFrame with inefficient datatypes
data = {'A': [1, 2, 3, 4],
        'B': [5.0, 6.0, 7.0, 8.0]}
df = pd.DataFrame(data)

# Replicate the DataFrame to create a larger dataset
df_large = pd.concat([df] * (num_rows // len(df)), ignore_index=True)

# Check memory usage before conversion
print("Memory usage before conversion:")
print(df_large.memory_usage().sum())

# Convert to more memory-efficient datatypes
df_large['A'] = pd.to_numeric(df_large['A'], downcast='integer')
df_large['B'] = pd.to_numeric(df_large['B'], downcast='float')

# Typecasting
df_large['A'] = df_large['A'].astype('int32')
df_large['B'] = df_large['B'].astype('float32')

# Check memory usage after conversion
print("Memory usage after conversion:")
print(df_large.memory_usage().sum())

# Print type casting
print("\nType casting:")
print("Column 'A' dtype:", df_large['A'].dtype)
print("Column 'B' dtype:", df_large['B'].dtype)
