# importing pandas as pd
import pandas as pd

# Creating the first dataframe
df1 = pd.DataFrame({"A":[1, 5, 7, 8],
					"B":[5, 8, 4, 3],
					"C":[10, 4, 9, 3]})

# Creating the second dataframe
df2 = pd.DataFrame({"A":[5, 3, 6, 4],
					"B":[11, 2, 4, 3],
					"C":[4, 3, 8, 5]})

# Print the first dataframe
print(df1, "\n")

# Print the second dataframe
print(df2)
