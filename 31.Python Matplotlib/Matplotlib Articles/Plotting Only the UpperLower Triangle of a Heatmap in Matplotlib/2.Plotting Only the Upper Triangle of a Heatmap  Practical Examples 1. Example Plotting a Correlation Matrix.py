import pandas as pd

df = pd.DataFrame({
    'A': np.random.rand(10),
    'B': np.random.rand(10),
    'C': np.random.rand(10),
    'D': np.random.rand(10),
    'E': np.random.rand(10)
})

# Calculate correlation matrix
corr_matrix = df.corr()

# Create upper triangle mask
mask = np.triu(np.ones_like(corr_matrix, dtype=bool))

# Apply mask to the correlation matrix
masked_corr = np.ma.array(corr_matrix, mask=mask)

plt.figure(figsize=(8, 6))
plt.title("Upper Triangle Correlation Matrix")
plt.imshow(masked_corr, interpolation='nearest', cmap='coolwarm', vmin=-1, vmax=1)
plt.colorbar()
plt.xticks(range(len(corr_matrix.columns)), corr_matrix.columns, rotation=90)
plt.yticks(range(len(corr_matrix.columns)), corr_matrix.columns)
plt.show()
