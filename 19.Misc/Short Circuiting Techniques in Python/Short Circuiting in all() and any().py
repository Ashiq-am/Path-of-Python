# python code to demonstrate short circuiting
# using all() and any()

# helper function
def check(i):
	print ("geeks")
	return i

# using all()
# stops execution when false occurs
# tells the compiler that even if one is
# false, all cannot be true, hence stop
# execution further.
# prints 3 "geeks"
print (all(check(i) for i in [1, 1, 0, 0, 3]))

print("\r")

# using any()
# stops execution when true occurs
# tells the compiler that even if one is
# true, expression is true, hence stop
# execution further.
# prints 4 "geeks"
print (any(check(i) for i in [0, 0, 0, 1, 3]))
