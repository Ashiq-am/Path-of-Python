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
	city: str = field(init=False, default="patna", repr=True,
					metadata={'format': 'State'})

emp = employee("Satyam", "ksatyam858", 21)
emp.__dataclass_fields__['city'].metadata['format']
