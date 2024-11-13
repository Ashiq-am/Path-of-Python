a1 = ((0, 1, 0, 1))
a = list(a1)

for x in range(len(a)):
	if(a[x]):
		a[x] = 0
	else:
		a[x] = 1

print(a)
