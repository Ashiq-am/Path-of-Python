# init field example
from dataclasses import dataclass, field


# A class for holding an employees content
@dataclass
class employee:
    # Attributes Declaration
    # using Type Hints
    name: str
    age: int

    # init field
    emp_id: str
    city: str = field(init=False, default="patna")


# object of dataclass
emp = employee("Satyam", "ksatyam858", 21)
print(emp)
