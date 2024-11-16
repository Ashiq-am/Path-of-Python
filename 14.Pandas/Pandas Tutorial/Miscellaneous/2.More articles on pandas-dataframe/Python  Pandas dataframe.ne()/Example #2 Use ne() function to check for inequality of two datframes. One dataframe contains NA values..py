# importing pandas as pd
import pandas as pd

# Creating the first dataframe
df1=pd.DataFrame({"A":[14,4,5,4,1],
				"B":[5,2,54,3,2],
				"C":[20,20,7,3,8],
				"D":[14,3,6,2,6]})

# Creating the second dataframe with <code>Na</code> value
df2=pd.DataFrame({"A":[12,4,5,None,1],
				"B":[7,2,54,3,None],
				"C":[20,16,11,3,8],
				"D":[14,3,None,2,6]})

# Print the second dataframe
df2
