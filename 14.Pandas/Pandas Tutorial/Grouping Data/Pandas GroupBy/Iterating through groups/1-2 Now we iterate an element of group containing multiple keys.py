# iterating an element
# of group containing
# multiple keys

grp = df.groupby(['Name', 'Qualification'])
for name, group in grp:
	print(name)
	print(group)
	print()
