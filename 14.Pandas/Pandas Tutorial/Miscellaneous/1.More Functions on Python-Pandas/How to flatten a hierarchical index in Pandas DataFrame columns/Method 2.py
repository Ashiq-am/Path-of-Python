# import the python pandas package
import pandas as pd

# create a sample dataframe
data = pd.DataFrame({"cars": ["bmw", "bmw", "benz", "benz"],
					"sale_q1 in Cr": [20, 22, 24, 26],
					'sale_q2 in Cr': [11, 13, 15, 17]},
					columns=["cars", "sale_q1 in Cr",
							'sale_q2 in Cr'])

# group by cars based on the
# sum of sales on quarter 1 and 2
# and mention as_index is False
grouped_data = data.groupby(by="cars", as_index=False).agg("sum")

# display
print(grouped_data)
