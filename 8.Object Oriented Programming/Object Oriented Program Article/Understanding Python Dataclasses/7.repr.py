# repr field
from dataclasses import dataclass, field

# A class for holding an employees content
@dataclass
class employee:

	# Attributes Declaration
	# using Type Hints
	name: str
	age: int
	emp_id: str
	city: str = field(init=False, default="patna", repr=True)

emp = employee("Satyam", 21, "ksatyam858"),
print(emp)
