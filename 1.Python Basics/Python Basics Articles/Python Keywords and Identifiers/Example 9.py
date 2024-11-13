# declare a variable
gvar = 10

# create a function
def fun1():
# print the value of gvar
	print(gvar)

# declare fun2()
def fun2():
# declare global value gvar
	global gvar
	gvar = 100

# call fun1()
fun1()

# call fun2()
fun2()
