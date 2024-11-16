# select the rows
# if Name column
# has special characters
print(df[df.Name.str.contains(r'[@#&$%+-/*]')])
