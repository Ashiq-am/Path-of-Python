a1 = ((0, 1, 0, 1))
a = list(a1)

for x in range(len(a)):
	# using Tilde operator(~)
	a[x] = ~a[x]

print(a)
