# default field example
from dataclasses import dataclass, field


# A class for holding an employees content
@dataclass
class employee:
    # Attributes Declaration
    # using Type Hints
    name: str
    emp_id: str
    age: int

    # default field set
    # city : str = "patna"
    city: str = field(default="patna")


emp = employee("Satyam", "ksatyam858", 21)
print(emp)
