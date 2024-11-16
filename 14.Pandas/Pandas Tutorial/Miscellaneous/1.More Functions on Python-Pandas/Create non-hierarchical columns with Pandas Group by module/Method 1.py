df_result = (df
		.groupby(['Sector','Industry'])
		.agg({'Employees':['sum', 'mean'],
				'Revchange':['min','max']}))

# printing top 15 rows
df_result.head(15)
