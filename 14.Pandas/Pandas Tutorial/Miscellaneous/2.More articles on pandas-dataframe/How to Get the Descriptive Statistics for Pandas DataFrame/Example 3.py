# Import package
from pandas import DataFrame

# Create DataFrame
cart = {'Product': ['Mobile', 'AC', 'Mobile', 'Sofa', 'Laptop'],
		'Price': [20000, 28000, 22000, 19000, 45000],
		'Year': [2014, 2015, 2016, 2017, 2018]
		}
df = DataFrame(cart, columns = ['Product', 'Price', 'Year'])

# Original DataFrame
print("Original DataFrame:\n", df)

# Describing descriptive statistics of whole dataframe
print("\nDescriptive statistics of whole dataframe:\n")
stats = df.describe(include = 'all')
print(stats)
