import numpy as np

# Create a DataFrame with random and constant columns
data = {
    'X1': np.random.randint(0, 100, size=100),
    'X2': [5] * 100,    # Constant column
    'X3': np.random.randint(0, 100, size=100),
    'X4': [3] * 100,    # Constant column
}

df_large = pd.DataFrame(data)

# Remove constant columns in the larger dataset
constant_columns = [col for col in df_large.columns if df_large[col].nunique() == 1]
df_large_cleaned = df_large.drop(columns=constant_columns)

print("Original DataFrame Shape:", df_large.shape)
print(df_large.head())
print()
print("Cleaned DataFrame Shape:", df_large_cleaned.shape)
print(df_large_cleaned.head())
