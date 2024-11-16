for category in all_categories:
    df[category] = df['Categories'].apply(lambda x: 1 if category in x else 0)

# Drop the original 'Categories' column
df = df.drop('Categories', axis=1)

print(df)
