# pandas version == 1.1.0 (min)
import pandas as pd
import numpy as np

# create your first DataFrame
# using pd.DataFrame
first_df = pd.DataFrame(
	{
		"Stationary": ["Pens", "Scales",
					"Pencils", "Geometry Box",
					"Crayon Set"],
		"Price": [100, 50, 25, 100, 65],
		"Quantity": [10, 5, 5, 2, 1]
	},
	columns=["Stationary", "Price", "Quantity"],
)
# Display the df
first_df
