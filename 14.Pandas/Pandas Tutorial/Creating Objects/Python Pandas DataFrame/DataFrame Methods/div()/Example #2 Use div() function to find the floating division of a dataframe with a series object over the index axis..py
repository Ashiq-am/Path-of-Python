# importing pandas as pd
import pandas as pd

# Creating the dataframe
df = pd.DataFrame({"A":[5, 3, 6, 4],
				"B":[11, 2, 4, 3],
				"C":[4, 3, 8, 5],
				"D":[5, 4, 2, 8]})

# Create a series object with no. of elements
# equal to the element along the index axis.

# Creating a pandas series object
series_object = pd.Series([2, 3, 1.5, 4])

# Print the series_obejct
series_object
