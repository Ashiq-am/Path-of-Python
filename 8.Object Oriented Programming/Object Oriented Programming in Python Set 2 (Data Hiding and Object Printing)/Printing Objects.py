#Printing objects gives us information about objects we are working with.
# In C++, we can do this by adding a friend ostream& operator << (ostream&, const Foobar&) method for the class.
# In Java, we use toString() method.
# In python this can be achieved by using __repr__ or __str__ methods.





class Test:
	def __init__(self, a, b):
		self.a = a
		self.b = b

	def __repr__(self):
		return "Test a:%s b:%s" % (self.a, self.b)

	def __str__(self):
		return "From str method of Test: a is %s," \ 
			"b is %s" % (self.a, self.b)

# Driver Code
t = Test(1234, 5678)
print(t) # This calls __str__()
print([t]) # This calls __repr__()








