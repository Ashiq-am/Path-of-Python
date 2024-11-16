df.agg({'Col_A' : ['sum', 'min'],
		'Col_B' : ['min', 'max'],
		'Col_C' : ['sum', 'mean']})
