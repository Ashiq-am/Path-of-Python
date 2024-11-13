#@gfg_decorator
def hello_decorator():
    print("Gfg")


'''Above code is equivalent to - 

def hello_decorator(): 
	print("Gfg") 

hello_decorator = gfg_decorator(hello_decorator)'''






"""In the above code, gfg_decorator is a callable function, 
will add some code on the top of some another callable function, hello_decorator function and return the wrapper function."""




