import pandas as pd

# Read CSV files
df1 = pd.read_csv('file1.csv')
df2 = pd.read_csv('file2.csv')

# Compare dataframes
diff = df1.compare(df2)

# Print the differences
print("Differences between file1 and file2:")
print(diff)
