# Defined class without any
# class methods and variables
class test:pass

# Defining method variables
test.x = 45

# Defining class methods
test.foo = lambda self: print('Hello')

# creating object
myobj = test()

print(myobj.x)
myobj.foo()

