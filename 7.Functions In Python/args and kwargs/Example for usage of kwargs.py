# Python program to illustrate
# *kargs for variable number of keyword arguments

def myFun(**kwargs):
	for key, value in kwargs.items():
		print ("%s == %s" %(key, value))

# Driver code
myFun(first ='Geeks', mid ='for', last='Geeks')








# Python program to illustrate **kargs for
# variable number of keyword arguments with
# one extra argument.

def myFun(arg1, **kwargs):
	for key, value in kwargs.items():
		print ("%s == %s" %(key, value))

# Driver code
myFun("Hi", first ='Geeks', mid ='for', last='Geeks')
