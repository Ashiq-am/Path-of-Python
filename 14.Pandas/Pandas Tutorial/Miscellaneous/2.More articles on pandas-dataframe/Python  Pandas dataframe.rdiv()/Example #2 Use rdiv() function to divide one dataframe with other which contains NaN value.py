# importing pandas as pd
import pandas as pd

# Creating the first dataframe
df1 = pd.DataFrame({"A":[1, 5, 3, 4, 2],
					"B":[3, 2, 4, 3, 4],
					"C":[2, 2, 7, 3, 4],
					"D":[4, 3, 6, 12, 7]})

# Creating the second dataframe
df2 = pd.DataFrame({"A":[14, 5, None, 4, 12],
					"B":[7, 6, 4, 5, None],
					"C":[2, 11, 4, 3, 6],
					"D":[4, None, 6, 2, 4]})

# divide df2 by df1 element-wise
# Fill all the missing values by 100
df1.rdiv(df2, fill_value = 100)
