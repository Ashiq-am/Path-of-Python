# function to take the data as group and perform aggregation
def totalTargets(group):
	g = group['target'].agg('sum')
	group['Total_targets'] = g
	return group

df_4 = df_3.groupby(df_3['Cat_mean_area']).apply(totalTargets)
df_4
