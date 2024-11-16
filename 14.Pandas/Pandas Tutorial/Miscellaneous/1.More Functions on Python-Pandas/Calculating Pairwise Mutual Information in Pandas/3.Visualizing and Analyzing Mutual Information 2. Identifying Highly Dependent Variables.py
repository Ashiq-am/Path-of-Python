# Get the top 10 pairs with the highest mutual information
top_pairs = mutual_info_df.unstack().sort_values(ascending=False).head(10)
print(top_pairs)
