# Reorder the categories in the DataFrame based on the sorted median
df['Category'] = pd.Categorical(df['Category'],
                                categories=category_median_sorted['Category'],
                                ordered=True)
