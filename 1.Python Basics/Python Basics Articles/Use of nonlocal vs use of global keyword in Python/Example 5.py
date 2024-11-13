var1 = 10
def fun():
	# new local variable var1
	# will be initialized in fun()
	var1 = 20
	print('var1 is', var1)
	print('var1 is at', id(var1))

fun()
print('var1 is', var1)
print('var1 is at', id(var1))
