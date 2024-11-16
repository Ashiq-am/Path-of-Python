# Names of ‘variable’ and ‘value’ columns can be customized
pd.melt(df, id_vars =['Name'], value_vars =['Course'],
			var_name ='ChangedVarname', value_name ='ChangedValname')
