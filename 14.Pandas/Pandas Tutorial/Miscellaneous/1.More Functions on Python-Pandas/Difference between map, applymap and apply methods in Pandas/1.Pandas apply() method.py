# Importing pandas library with an alias pd
import pandas as pd

# Dataframe generation
gfg_string = 'geeksforgeeks'
gfg_list = 5 * [pd.Series(list(gfg_string))]

gfg_df = pd.DataFrame(data = gfg_list)
print("Original dataframe:\n" + \
	gfg_df.to_string(index = False,
	header = False), end = '\n\n')

# Using apply method for sorting
# rows of characters present in
# the original dataframe
new_gfg_df = gfg_df.apply(lambda x:x.sort_values(), axis = 1)

print("Transformed dataframe:\n" + \
	new_gfg_df.to_string(index = False,
			header = False), end = '\n\n')
