#%%timeit -n 100

even =[ ]
for i in range(10**7):
	if i % 2 == 0:
		even.append(i)
