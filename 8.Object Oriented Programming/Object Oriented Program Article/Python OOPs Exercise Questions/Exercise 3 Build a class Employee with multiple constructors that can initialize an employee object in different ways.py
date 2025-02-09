class Employee:
    def __init__(self, name, id=None, department=None):
        self.name = name
        self.id = id
        self.department = department

    def display_details(self):
        print(f"Name: {self.name}")
        if self.id:
            print(f"ID: {self.id}")
        if self.department:
            print(f"Department: {self.department}")

# Examples
emp1 = Employee("John")
emp1.display_details()

emp2 = Employee("Doe", 101)
emp2.display_details()

emp3 = Employee("Jane", 102, "HR")
emp3.display_details()
