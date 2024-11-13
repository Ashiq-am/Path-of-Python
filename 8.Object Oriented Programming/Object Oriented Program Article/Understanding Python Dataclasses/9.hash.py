# hash
from dataclasses import dataclass, field

# A class for holding an employees content
@dataclass(unsafe_hash=True)
class employee:

	# Attributes Declaration
	# using Type Hints
	name: str
	age: int
	emp_id: str = field(default_factory=get_emp_id)
	city: str = field(init=False, default="patna", repr=True, hash=True)

emp = employee("Satyam", "ksatyam858", 21)
hash(emp)
