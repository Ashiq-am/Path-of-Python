import pandas as pd
# Sample DataFrame with custom index
data = {'Product': ['Laptop', 'Smartphone', 'Tablet'],'Price': [1000, 800, 400],'Stock': [10, 20, 15]}
df = pd.DataFrame(data)

# Setting 'Product' as the index
df.set_index('Product', inplace=True)
# Reset the index, keeping the old index as a column
df_reset = df.reset_index(drop=False)
print("\nDataFrame after reset_index:")
print(df_reset)