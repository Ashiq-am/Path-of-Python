# explicit function
def fun(a, b):
	return a**b

# import required modules
import inspect

# use getargspec()
print(inspect.getargspec(fun))
