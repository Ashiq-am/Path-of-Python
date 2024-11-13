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


# object of the class
emp = employee("Satyam", "ksatyam858", 21, 'Patna')

emp.__dataclass_fields__
