# A basic Data Class
# importing dataclass module
from dataclasses import dataclass, field


# parent class
@dataclass
class Staff:
	name: str
	emp_id: str
	age: int

# child class
@dataclass
class employee(Staff):
	salary: int


emp = employee("Satyam", "ksatyam858", 21, 60000)
emp
