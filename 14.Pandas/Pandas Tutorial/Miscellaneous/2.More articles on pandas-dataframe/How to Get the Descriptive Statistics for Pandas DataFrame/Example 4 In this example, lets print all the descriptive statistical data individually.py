from pandas import DataFrame

# Create DataFrame
cart = {'Product': ['Mobile', 'AC', 'Mobile', 'Sofa', 'Laptop'],
		'Price': [20000, 28000, 22000, 19000, 45000],
		'Year': [2014, 2015, 2016, 2017, 2018]
		}
df = DataFrame(cart, columns = ['Product', 'Price', 'Year'])

# Original DataFrame
print("Original DataFrame:\n", df)

# Print Count of Price
print("\nCount of Price:\n")
counts = df['Price'].count()
print(counts)

# Print mean of Price
print("\nMean of Price:\n")
m = df['Price'].mean()
print(m)

# Print maximum value of Price
print("\nMaximum value of Price:\n")
mx = df['Price'].max()
print(m)

# Print standard deviation of Price
print("\nStandard deviation of Price:\n")
sd = df['Price'].std()
print(sd)
