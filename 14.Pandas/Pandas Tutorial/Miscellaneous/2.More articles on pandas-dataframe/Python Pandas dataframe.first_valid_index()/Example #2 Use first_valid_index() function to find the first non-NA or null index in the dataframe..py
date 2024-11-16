# importing pandas as pd
import pandas as pd

# Creating the dataframe
df = pd.DataFrame({"A":[None, None, 2, 4, 5],
				"B":[None, None, None, 44, 2],
				"C":[None, None, None, 1, 5]})

# applying first_valid_index() function
df.first_valid_index()
