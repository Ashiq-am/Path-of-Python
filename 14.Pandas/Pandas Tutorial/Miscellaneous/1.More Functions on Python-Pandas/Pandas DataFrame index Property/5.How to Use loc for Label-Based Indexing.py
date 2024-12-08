import pandas as pd
data = {'Product': ['Laptop', 'Smartphone', 'Tablet'],'Price': [1000, 800, 400],}
df = pd.DataFrame(data)

# Modify the index by setting the 'Product' column as the index
df.set_index('Product', inplace=True)

# Display the DataFrame with 'Product' as the index
print("DataFrame with 'Product' as the index:")
print(df.loc['Laptop':'Smartphone'])