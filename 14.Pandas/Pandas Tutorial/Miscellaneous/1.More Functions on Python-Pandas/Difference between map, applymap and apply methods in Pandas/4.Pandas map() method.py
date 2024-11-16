# Importing pandas library with an alias pd
import pandas as pd

# Series generation
gfg_string = 'geeksforgeeks'
gfg_series = pd.Series(list(gfg_string))
print("Original series\n" + \
	gfg_series.to_string(index = False,
			header = False), end = '\n\n')

# Using apply method for converting characters
# present in the original series
new_gfg_series = gfg_series.map(str.upper)
print("Transformed series:\n" + \
	new_gfg_series.to_string(index = False,
				header = False), end = '\n\n')
