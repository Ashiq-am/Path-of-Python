# Importing pandas as pd
from pandas import DataFrame

# Creating a data frame
cart = {'Product': ['Mobile', 'AC', 'Laptop', 'TV', 'Football'],
		'Type': ['Electronic', 'HomeAppliances', 'Electronic',
				'HomeAppliances', 'Sports'],
		'Price': [10000, 35000, 50000, 30000, 799]
	}

df = DataFrame(cart, columns = ['Product', 'Type', 'Price'])

# Print original data frame
print("Original data frame:\n")
print(df)

# Selecting the product of Price greater
# than or equal to 25000
select_prod = df.loc[df['Price'] >= 25000]

print("\n")

# Print selected rows based on the condition
print("Selecting rows:\n")
print (select_prod)
