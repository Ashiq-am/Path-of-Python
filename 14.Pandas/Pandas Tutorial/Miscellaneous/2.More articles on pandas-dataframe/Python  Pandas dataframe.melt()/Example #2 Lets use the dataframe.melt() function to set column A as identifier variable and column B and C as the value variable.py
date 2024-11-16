# function to unpivot the dataframe
# We will also provide a customized name to the value and variable column

df.melt(id_vars =['A'], value_vars =['B', 'C'],
		var_name ='Variable_column', value_name ='Value_column')
