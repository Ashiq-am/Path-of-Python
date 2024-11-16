# importing pandas as pd
import pandas as pd

# Creating a dataframe using dictionary

df = pd.DataFrame({"A":[-5, 8, 12, -9, 5, 3],
				"B":[-1, -4, 6, 4, 11, 3],
				"C":[11, 4, -8, 7, 3, -2]})

# lower limit for each individual column element.
limit = np.array([[1, 2, 3], [10, 12, 3], [1, 4, 3],
				[1, 2, 3], [1, 2, 3], [1, 2, 3]])

# Print lower_limit
limit
