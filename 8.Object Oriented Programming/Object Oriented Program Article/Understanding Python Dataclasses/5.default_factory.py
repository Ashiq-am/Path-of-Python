# default factory example
from dataclasses import dataclass, field


def get_emp_id():
    id = 2345
    return id


# A class for holding an employees content
@dataclass
class employee:
    # Attributes Declaration
    # using Type Hints
    name: str
    age: int

    # default factory field
    emp_id: str = field(default_factory=get_emp_id)
    city: str = field(default="patna")


# object of dataclass
emp = employee("Satyam", 21)
print(emp)
