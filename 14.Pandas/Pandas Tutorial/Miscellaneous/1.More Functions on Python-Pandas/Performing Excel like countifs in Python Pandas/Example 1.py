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
twills_Shirt_Count = costumes.query('Brand=="Twills" \
& Costume_Type=="Shirt"')['Costume_Type'].count()

print('Number of Twills Shirts-', end="")
print(twills_Shirt_Count)
