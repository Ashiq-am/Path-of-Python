ls = []

for i in s:
	ls.extend(i)

s1 = pd.Series(ls)
print(s1)
