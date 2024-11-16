# import necessary packages
import pandas as pd

# create a dataframe
costumes = pd.DataFrame({'Brand': ['Twills', 'Wrogn',
								'Twills', 'Trigger',
								'Twills', 'Wrogn', ],
						'Costume_Type': ['Shirt', 'Shirt',
										'Shirt', 'Jeans',
										'T-Shirt', 'Jeans'],
						'price': [1699, 1999, 1569,
								2000, 569, 2400]})

# DataFrame
print(costumes)

# find count of Twills Shirts
Jeans_Count = costumes.query('Costume_Type=="Jeans" & price<=2000')[
	'Costume_Type'].count()

print('\nNumber of Jeans below or equals to Rs.2000-', end=" ")
print(Jeans_Count)
