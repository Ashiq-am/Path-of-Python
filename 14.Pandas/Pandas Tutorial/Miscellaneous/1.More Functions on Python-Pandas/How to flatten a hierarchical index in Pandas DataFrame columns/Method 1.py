# import the python pandas package
import pandas as pd

# create a sample dataframe
data = pd.DataFrame({"cars": ["bmw", "bmw", "benz", "benz"],
                     "sale_q1 in Cr": [20, 22, 24, 26],
                     'sale_q2 in Cr': [11, 13, 15, 17]},

                    columns=["cars", "sale_q1 in Cr",
                             'sale_q2 in Cr'])

# group by cars based on the sum
# of sales on quarter 1 and 2
grouped_data = data.groupby(by="cars").agg("sum")

print(grouped_data)

# use reset_index to flattend
# the hierarchical dataframe.
flat_data = grouped_data.reset_index()

print(flat_data)
