# class for holding person's details
class person:

	# constructor
	def __init__(self, name, age, des):
		self.name = name
		self.age = age
		self.des = des

	# overriding format()
	def __format__(self, f):

		if f == 'name':
			return "I am "+self.name

		if f == 'age':
			return "My age is "+str(self.age)

		if f == 'des':
			return "I work as "+self.des


p = person('nisha', 23, 'manager')
print("{:name}, {:age}".format(p, p))
print("{:des}".format(p))
