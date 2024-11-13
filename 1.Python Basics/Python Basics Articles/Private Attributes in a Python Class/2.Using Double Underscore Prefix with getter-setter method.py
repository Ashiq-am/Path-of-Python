class Student:
	def __init__(self, name, id):
		self.__id = id
		self.name = name

	def get_Id(self):
		return self.__id

# Setting the data of the student
sonali = Student("Sonali Kumari", 58)

# Printing the name as the name is public
print("The name is :", sonali.name)

# Printing the Id by getter method as the id is private
print("The id is :", sonali.get_Id())
