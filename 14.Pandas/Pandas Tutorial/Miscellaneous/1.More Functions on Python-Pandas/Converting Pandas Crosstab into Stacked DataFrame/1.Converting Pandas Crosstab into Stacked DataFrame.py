# import the numpy and pandas package
import numpy as np
import pandas as pd

# create three seperate arrays namely car_brand,
# version, fuel_type as shown
car_brand = np.array(["bmw", "bmw", "bmw", "bmw", "benz", "benz",
					"bmw", "bmw", "benz", "benz", "benz", "benz",
					"bmw", "bmw", "bmw", "benz", "benz", ],
					dtype=object)

version = np.array(["one", "one", "one", "two", "one", "one", "one",
					"two", "one", "one", "one", "two", "two", "two",
					"one", "two", "one"], dtype=object)

fuel_type = np.array(["petrol", "petrol", "petrol", "diesel", "diesel",
					"petrol", "diesel", "diesel", "diesel", "petrol",
					"petrol", "diesel", "petrol", "petrol", "petrol",
					"diesel", "diesel", ],
					dtype=object)

# use pandas crosstab and pass the three
# arrays as index and columns
# to create a crosstab table.
cross_tab_data = pd.crosstab(index=car_brand,
							columns=[version, fuel_type],
							rownames=['car_brand'],
							colnames=['version', 'fuel_type'])

barplot = cross_tab_data.plot.bar()

# use the created sample crosstab data
# to convert it to a stacked dataframe
stacked_data = cross_tab_data.stack(level=1)

print(stacked_data)
