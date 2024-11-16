# Compute the median for each category
category_median = df.groupby('Category')['Values'].median().reset_index()

# Sort the categories by the median
category_median_sorted = category_median.sort_values(by='Values')
