# importing pandas as pd
import pandas as pd

# Creating the first dataframe
df = pd.DataFrame({"A":["Sandy", "alex", "brook", "kelly", np.nan],
				"B":[np.nan, "olivia", "olivia", "", "amanda"],
				"C":[20 + 5j, 20 + 5j, 7, None, 8],
				"D":[14.8, 3, None, 6, 6]})

# apply the nunique() function
df.nunique(axis = 0, dropna = True)
