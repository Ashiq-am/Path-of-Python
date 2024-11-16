# importing pandas as pd
import pandas as pd

# Creating the dataframe
df = pd.DataFrame({"A":["Sandy", "alex", "brook", "kelly", np.nan],
				"B":[np.nan, "olivia", "terica", "", "amanda"],
				"C":[20 + 5j, 20 + 3j, 7, None, 8],
					"D":[14.8, 3, None, 2.3, 6]})

# find non-missing values
df.notnull()
