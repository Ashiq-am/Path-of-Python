# import the numpy and pandas package
import numpy as np
import pandas as pd

# create three seperate arrays namely car_brand,
# version, fuel_type as shown
car_brand = np.array(["bmw", "bmw", "bmw", "bmw", "benz",
					"benz", "bmw", "bmw", "benz", "benz",
					"benz", "benz", "bmw", "bmw", "bmw",
					"benz", "benz", ], dtype=object)

version = np.array(["one", "one", "one", "two", "one", "one",
					"one", "two", "one", "one", "one", "two",
					"two", "two", "one", "two", "one"],
				dtype=object)

fuel_type = np.array(["petrol", "petrol", "petrol", "diesel",
					"diesel", "petrol", "diesel", "diesel",
					"diesel", "petrol", "petrol", "diesel",
					"petrol", "petrol", "petrol", "diesel",
					"diesel", ], dtype=object)

year_release = np.array([2000, 2005, 2000, 2007, 2000, 2005,
						2007, 2005, 2005, 2000, 2007, 2000,
						2007, 2005, 2005, 2007, 2000],
						dtype=object)

# use pandas crosstab and pass the three arrays
# as index and columns to create a crosstab table.
cross_tab_data = pd.crosstab(index=car_brand,
							columns=[version, fuel_type, year_release],
							rownames=['car_brand'],
							colnames=['version', 'fuel_type', 'year_release'])

barplt = cross_tab_data.plot.bar()

# use the created sample crosstab data to
# convert it to a stacked dataframe with
# level 1
stacked_data = cross_tab_data.stack(level=1)


barplot = stacked_data.plot.bar()

# use the created sample crosstab data to
# convert it to a stacked dataframe with
# level 2
stacked_data = cross_tab_data.stack(level=2)

barplot = stacked_data.plot.bar()
