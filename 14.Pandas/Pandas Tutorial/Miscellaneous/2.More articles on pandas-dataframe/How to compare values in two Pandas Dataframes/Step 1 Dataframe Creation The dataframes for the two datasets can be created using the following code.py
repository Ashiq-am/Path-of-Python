import pandas as pd


# elements of first dataset
first_Set = {'Prod_1': ['Laptop', 'Mobile Phone',
						'Desktop', 'LED'],
			'Price_1': [25000, 8000, 20000, 35000]
				}

# creation of Dataframe 1
df1 = pd.DataFrame(first_Set, columns = ['Prod_1', 'Price_1'])
print(df1)

# elements of second dataset
second_Set = {'Prod_2': ['Laptop', 'Mobile Phone',
						'Desktop', 'LED'],
			'Price_2': [25000, 10000, 15000, 30000]
					}

# creation of Dataframe 2
df2 = pd.DataFrame(second_Set, columns = ['Prod_2', 'Price_2'])
print (df2)
