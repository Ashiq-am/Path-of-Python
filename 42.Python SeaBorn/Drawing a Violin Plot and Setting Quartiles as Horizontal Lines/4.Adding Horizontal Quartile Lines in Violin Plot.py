# Function to calculate quartiles
def calculate_quartiles(group):
    return np.percentile(group, [25, 50, 75])

# Calculate quartiles for each category
quartiles = data.groupby('Category')['Values'].apply(calculate_quartiles)
