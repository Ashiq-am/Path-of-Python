class sample(object):

	# Static variable for object number
	objectNo = 0

	def __init__(self, name1):
		# variable to hold name
		self.name = name1

		# Increment static variable for each object
		sample.objectNo = sample.objectNo + 1

		# each object's unique number that can be
		# considered as ID
		self.objNumber = sample.objectNo

	def myFunc(self):
		print("My name is ", self.name,
			"from object ", self.objNumber)

	def alterIt(self, newName):
		self.name = newName

	# using decorator to make the method static
	@staticmethod
	def myFunc2():
		print("I am not a bound method !!!")


# creating first instance of class sample
samp1 = sample("A")
samp1.myFunc()


sample.myFunc2() #----------> error line


# creating second instance of class sample
samp2 = sample("B")
samp2.myFunc()
samp2.alterIt("C")
samp2.myFunc()
samp1.myFunc()
