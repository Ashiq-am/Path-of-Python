# Python 3 code to demonstrate
# working of isinstance()
# with objects

# declaring classes
class gfg1:
	a = 10

# inherited class
class gfg2(gfg1):
	string = 'GeeksforGeeks'


# initializing objects
obj1 = gfg1()
obj2 = gfg2()

# checking instances
print("Is obj1 instance of gfg1? : " + str(isinstance(obj1, gfg1)))
print("Is obj2 instance of gfg2? : " + str(isinstance(obj2, gfg2)))
print("Is obj1 instance of gfg2? : " + str(isinstance(obj1, gfg2)))


# check inheritance case
# return true
print("Is obj2 instance of gfg1? : " + str(isinstance(obj2, gfg1)))
