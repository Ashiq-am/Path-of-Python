import pandas as pd

# Sample DataFrames
df_store_a = pd.DataFrame({'Product': ['Shirt', 'Pants'], 'Sales': [100, 200]})
df_store_b = pd.DataFrame({'Product': ['Shirt', 'Hat'], 'Sales': [150, 50]})

# Merge DataFrames based on 'Product'
merged_df = df_store_a.merge(df_store_b, on='Product', how='inner')

# Group by 'Product' and sum 'Sales'
total_sales = merged_df.groupby('Product')['Sales'].sum()

# Print the total sales
print(total_sales)
