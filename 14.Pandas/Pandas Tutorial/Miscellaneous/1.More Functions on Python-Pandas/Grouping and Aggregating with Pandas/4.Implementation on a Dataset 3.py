# dictionary having key as group name of price and
# value as list of aggregation function
# we want to perform on group price
agg_functions = {
	'price':
	['sum', 'mean', 'median', 'min', 'max', 'prod']
}

dataset.groupby(['color']).agg(agg_functions)
