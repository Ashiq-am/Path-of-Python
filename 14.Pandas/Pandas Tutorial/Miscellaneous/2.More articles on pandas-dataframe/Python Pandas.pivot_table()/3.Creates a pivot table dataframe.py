# Creates a pivot table dataframe
table = pd.pivot_table(df, values ='A', index =['B', 'C'],
						columns =['B'], aggfunc = np.sum)

table
