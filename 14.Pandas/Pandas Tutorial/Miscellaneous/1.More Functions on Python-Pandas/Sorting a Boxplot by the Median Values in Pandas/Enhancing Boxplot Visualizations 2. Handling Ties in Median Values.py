# Compute both median and mean to handle ties
category_stats = df.groupby('Category').agg({'Values': ['median', 'mean']}).reset_index()
category_stats.columns = ['Category', 'Median', 'Mean']

# Sort by median and then by mean in case of ties
category_stats_sorted = category_stats.sort_values(by=['Median', 'Mean'])
print(category_stats.columns)
