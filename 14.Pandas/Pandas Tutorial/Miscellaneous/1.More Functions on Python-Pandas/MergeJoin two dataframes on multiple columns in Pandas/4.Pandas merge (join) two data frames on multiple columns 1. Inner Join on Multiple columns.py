import pandas as pd

df1 = pd.DataFrame({'product_code': ['P001', 'P002', 'P003'],'store_location': ['New York', 'Los Angeles', 'Chicago'],'stock_quantity': [120, 150, 200]})
df2 = pd.DataFrame({'product_code': ['P001', 'P002', 'P004'],'store_location': ['New York', 'Los Angeles', 'Houston'],'price': [15.5, 20.0, 25.0]})

# Merge DataFrames on 'product_code' and 'store_location'
merged_df = pd.merge(df1, df2, on=['product_code', 'store_location'], how='inner')
print(merged_df)