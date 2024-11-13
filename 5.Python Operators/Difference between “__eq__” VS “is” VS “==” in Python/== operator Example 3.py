class Student:
	def __init__(self, name):
		self.name = name

	def __eq__(self, other):
		if isinstance(other, Student):
			if other.name == self.name:
				return True
		return False


divyansh = Student("Divyansh")
shivansh = Student("Divyansh")

print("divyansh == shivansh : ", (divyansh == shivansh))
