#python code for creating tuples in a loop

tup = ('geek',)
n = 5 #Number of time loop runs
for i in range(int(n)):
	tup = (tup,)
	print(tup)
