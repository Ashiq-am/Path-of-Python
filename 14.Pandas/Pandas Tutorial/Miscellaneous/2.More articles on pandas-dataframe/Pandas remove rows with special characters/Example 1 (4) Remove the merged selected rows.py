# drop the merged selected rows
print(df.drop(df[df.Name.str.contains(r'[^0-9a-zA-Z]')
				| df.Grade.str.contains(r'[^0-9a-zA-Z]')].index))
