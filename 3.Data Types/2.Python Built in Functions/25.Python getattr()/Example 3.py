# Python code to demonstrate
# performance analysis of getattr()
import time

# declaring class
class GfG:
	name = "GeeksforGeeks"
	age = 24

# initializing object
obj = GfG()

# use of getattr to print name
start_getattr = time.time()
print("The name is " + getattr(obj, 'name'))
print("Time to execute getattr " + str(time.time() - start_getattr))

# use of conventional method to print name
start_obj = time.time()
print("The name is " + obj.name)
print("Time to execute conventional method " + str(time.time() - start_obj))
