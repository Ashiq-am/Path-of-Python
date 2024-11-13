# Python code for accessing attributes of class
class emp:
	name='Harsh'
	salary='25000'
	def show(self):
		print(self.name)
		print(self.salary)
e1 = emp()
# Use getattr instead of e1.name
print(getattr(e1,'name'))

# returns true if object has attribute
print(hasattr(e1,'name'))

# sets an attribute
setattr(e1,'height',152)

# returns the value of attribute name height
print(getattr(e1,'height'))

# delete the attribute
delattr(emp,'salary')
