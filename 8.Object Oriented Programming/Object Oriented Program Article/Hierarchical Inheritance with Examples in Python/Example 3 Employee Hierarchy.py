class Employee:
	def __init__(self, name, salary):
		self.name = name
		self.salary = salary

	def display_details(self):
		return f"Name: {self.name}, Salary: {self.salary}"

class Manager(Employee):
	def __init__(self, name, salary, team_size):
		super().__init__(name, salary)
		self.team_size = team_size

	def display_details(self):
		return f"{super().display_details()}, Team Size: {self.team_size}"

class Developer(Employee):
	def __init__(self, name, salary, programming_language):
		super().__init__(name, salary)
		self.programming_language = programming_language

	def display_details(self):
		return f"{super().display_details()}, Language: {self.programming_language}"

# Usage
manager = Manager("John", 80000, 10)
developer = Developer("Alice", 60000, "Python")
print(manager.display_details())
print(developer.display_details())
