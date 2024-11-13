# A basic Data Class
# importing dataclass module
from dataclasses import dataclass

# A class for holding an employees content
@dataclass
class employee:

	# Attributes Declaration
	# using Type Hints
	name: str
	emp_id: str
	age: int
	city: str


emp1 = employee("Satyam", "ksatyam858", 21, 'Patna')
emp2 = employee("Anurag", "au23", 28, 'Delhi')
emp3 = employee("Satyam", "ksatyam858", 21, 'Patna')

print("employee object are :")
print(emp1)
print(emp2)
print(emp3)

# printing new line
print()

# referring two object to check equality
print("Data in emp1 and emp2 are same? ", emp1 == emp2)
print("Data in emp1 and emp3 are same? ", emp1 == emp3)
