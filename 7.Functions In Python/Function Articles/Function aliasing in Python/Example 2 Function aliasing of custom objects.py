class Test:
	def __init__(self):
		self.u_name = "user-origin"

	def name(self):
		return self.u_name


# create object of Test class
test = Test()

# create function refence and it's alias
name_fn = test.name
name_fn_ref = name_fn

# this will print user-origin
print(name_fn())

test.u_name = "user-mod"

# this will print user-mod
print(name_fn_ref())
