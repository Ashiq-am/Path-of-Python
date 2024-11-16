data = {'FRUITS': ['Grapes', 'Pineapple'],
		'QUANTITY': [23, 17],
		'PRICE': [60, 30]
		}

# Create Pandas Dataframe with dictionary
df1 = pd.DataFrame(data)

# Concatenate df and df1
df2 = pd.concat([df, df1], axis=0,
				ignore_index=True)
print(df2)
