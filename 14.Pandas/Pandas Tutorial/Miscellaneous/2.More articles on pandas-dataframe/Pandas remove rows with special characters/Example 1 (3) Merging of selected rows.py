# merge the selected rows
# by using or
print(df[df.Name.str.contains(r'[^0-9a-zA-Z]')
		| df.Grade.str.contains(r'[@#&$%+-/*]')])
