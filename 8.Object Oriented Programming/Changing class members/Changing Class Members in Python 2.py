# Program to show how to make changes to the
# class variable in Python

# Class for Computer Science Student
class CSStudent:
	stream = 'cse'	 # Class Variable
	def __init__(self, name, roll):
		self.name = name
		self.roll = roll

# New object for further implementation
a = CSStudent("check", 3)
print("a.tream =", a.stream)

# Correct way to change the value of class variable
CSStudent.stream = "mec"
print("\nClass variable changes to mec")

# New object for further implementation
b = CSStudent("carter", 4)

print("\nValue of variable steam for each object")
print("a.stream =", a.stream)
print("b.stream =", b.stream)
