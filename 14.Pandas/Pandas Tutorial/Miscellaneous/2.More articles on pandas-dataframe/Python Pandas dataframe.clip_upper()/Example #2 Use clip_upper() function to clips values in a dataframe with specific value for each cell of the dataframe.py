# importing pandas as pd
import pandas as pd

# Creating a dataframe using dictionary

df = pd.DataFrame({"A":[-5, 8, 12, -9, 5, 3],
				"B":[-1, -4, 6, 4, 11, 3],
				"C":[11, 4, -8, 7, 3, -2]})

# upper limit for each individual column element.
limit = np.array([[10, 2, 8], [3, 5, 3], [2, 4, 6],
				[11, 2, 3], [5, 2, 3], [4, 5, 3]])

# Print upper_limit
limit
