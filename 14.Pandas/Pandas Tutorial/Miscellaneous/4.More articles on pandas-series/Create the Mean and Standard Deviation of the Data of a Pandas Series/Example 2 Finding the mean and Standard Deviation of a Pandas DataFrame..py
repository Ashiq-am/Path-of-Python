# importing the module
import pandas as pd

# creating a dataframe
df = pd.DataFrame({'ID':[114, 345, 157788, 5626],
				'Product':['shirt', 'trousers', 'tie', 'belt'],
				'Color':['White', 'Black', 'Red', 'Brown'],
				'Discount':[10, 10, 10, 10]})

# displaying the DataFrame
print(df)
