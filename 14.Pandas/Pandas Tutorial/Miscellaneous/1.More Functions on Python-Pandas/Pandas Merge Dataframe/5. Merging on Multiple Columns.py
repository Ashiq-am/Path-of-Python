# Example with additional columns
df1['Country'] = ['USA', 'Canada', 'USA', 'Canada', 'USA']
df2['Country'] = ['USA', 'Canada', 'USA', 'Canada', 'Mexico']

# Merge on 'ID' and 'Country'
merged_df = pd.merge(df1, df2, on=['ID', 'Country'], how='inner')
print(merged_df)