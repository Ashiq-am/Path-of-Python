# A basic Data Class
# importing dataclass module
from dataclasses import dataclass, field


# A class for holding an employees content
@dataclass
class employee:

	# Attributes Declaration
	# using Type Hints
	name: str
	emp_id: str
	age: int
	city: str

	# post init function
	def __post_init__(self):
		if self.age >= 30:
			self.check_age = True
		else:
			self.check_age = False


emp = employee("Satyam", "ksatyam858", 21, 'Patna')
emp.check_age
