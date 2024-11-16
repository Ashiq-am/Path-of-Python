ls = []
for i in s:
	ls.append(pd.Series(i))

s1 = pd.concat([*ls]).reset_index(drop = True)

print(s1)
