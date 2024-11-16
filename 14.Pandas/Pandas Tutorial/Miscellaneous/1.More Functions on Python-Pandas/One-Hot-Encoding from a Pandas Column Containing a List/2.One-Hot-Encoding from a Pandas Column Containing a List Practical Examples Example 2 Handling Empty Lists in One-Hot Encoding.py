# Step 1: Create a DataFrame with some empty lists
data = {
    'ID': [1, 2, 3, 4],
    'Items': [['A', 'B'], ['B'], [], ['C', 'D']]
}
df = pd.DataFrame(data)

# Step 2: One-hot encoding with empty list handling
one_hot = pd.get_dummies(df['Items'].apply(pd.Series).stack()).groupby(level=0).sum()

# Ensure rows with empty lists are handled
df_one_hot = df.drop('Items', axis=1).join(one_hot, how='left').fillna(0).astype(int)

print(df_one_hot)
