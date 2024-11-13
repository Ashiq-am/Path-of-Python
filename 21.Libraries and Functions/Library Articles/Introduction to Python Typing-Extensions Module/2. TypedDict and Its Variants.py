from typing_extensions import NotRequired

class EmployeeOptional(TypedDict):
    name: str
    age: NotRequired[int]  # Optional field

employee = EmployeeOptional(name="Arun")
print(employee)
