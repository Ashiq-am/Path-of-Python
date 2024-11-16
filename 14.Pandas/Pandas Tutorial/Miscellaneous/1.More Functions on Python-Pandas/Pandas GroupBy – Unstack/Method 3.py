# import the python pandas package
import pandas as pd
# create a sample dataframe
data = pd.DataFrame({"cars": ["bmw", "bmw", "benz", "benz"],
					"sale_q1 in Cr": [20, 22, 24, 26],
					'sale_q2 in Cr': [11, 13, 15, 17]},
					columns=["cars", "sale_q1 in Cr",
							'sale_q2 in Cr'])
print(data)

# aggregate the car sales data by sum min and
# max sales of two quarters as shown
grouped_data = data.groupby('cars').agg(
	{"sale_q1 in Cr": [sum, max], "sale_q2 in Cr": [sum, min]})
print(grouped_data)

# stacking the grouped dataframe at
# differenet levels and unstacking
# unstacking the stacked dataframe at level = 0
unstack_level1 = grouped_data.stack(level=0).unstack()
print(unstack_level1)

# unstacking the stacked dataframe at level =1
unstack_level2 = grouped_data.stack(level=1).unstack()
print(unstack_level2)
