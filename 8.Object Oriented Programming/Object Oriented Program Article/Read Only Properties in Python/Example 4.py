class employee:
    def __init__(self, basesalary, yearsofworking):
        self.basesalary = basesalary
        self.yearsofworking = yearsofworking
        self._salary = 0

    @property
    def salary(self):
        return self._salary

    @salary.setter
    def salary(self, salary):
        self._salary = salary


amit = employee(20000, 5)
amit.salary = 10000
print(amit.basesalary, amit.yearsofworking, amit.salary)
