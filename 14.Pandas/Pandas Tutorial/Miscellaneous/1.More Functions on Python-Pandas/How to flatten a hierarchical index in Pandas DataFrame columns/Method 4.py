# import the python pandas package
import pandas as pd

# create a sample dataframe
data = pd.DataFrame({"cars": ["bmw", "bmw", "benz", "benz"],

					"sale_q1 in Cr": [20, 22, 24, 26],

					'sale_q2 in Cr': [11, 13, 15, 17]},

					columns=["cars", "sale_q1 in Cr",
							'sale_q2 in Cr'])

# group by cars based on the sum
# and max of sales on quarter 1
# and sum and min of sales 2 and mention
# as_index is False
grouped_data = data.groupby(by="cars").agg({"sale_q1 in Cr": [sum, max],
											'sale_q2 in Cr': [sum, min]})
# use to_records function on grouped data
# and pass this to the Dataframe function
flattened_data = pd.DataFrame(grouped_data.to_records())

print(flattened_data)
