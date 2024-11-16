flatdata = pd.DataFrame([( index, value) for ( index, values)
						in df[ 'A' ].iteritems() for value in values],
							columns = [ 'index', 'A']).set_index( 'index' )

df = df.drop( 'A', axis = 1 ).join( flatdata )
display(df)
