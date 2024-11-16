# importing pandas as pd
import pandas as pd

# Creating the first dataframe
df1 = pd.DataFrame({"A":[1, 5, 3, 4, 2],
					"B":[3, 2, 4, 3, 4],
					"C":[2, 2, 7, 3, 4],
					"D":[4, 3, 6, 12, 7]})

# reindexing the column axis with
# old and new index values
df.reindex(columns =["A", "B", "D", "E"])
