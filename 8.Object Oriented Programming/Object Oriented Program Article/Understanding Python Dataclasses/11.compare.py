# hash
from dataclasses import dataclass, field

# A class for holding an employees content
@dataclass(unsafe_hash=True)
class employee:

	# Attributes Declaration
	# using Type Hints
	name: str
	age: int
	emp_id: str
	city: str = field(init=False, default="patna",
					repr=True, hash=False, compare=True)


emp1 = employee("Satyam", "ksatyam858", 21)
emp2 = employee("Kumar", "satyam.10151", 22)
emp1 == emp2
