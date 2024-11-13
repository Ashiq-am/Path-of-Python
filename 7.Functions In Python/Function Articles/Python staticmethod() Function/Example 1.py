class demoClass:

	def greet(msg):
		return msg


# covert the add to a static method
demoClass.greet = staticmethod(demoClass.greet)

# we can access the method without
# creating the instance of class
print(demoClass.greet("hai"))
