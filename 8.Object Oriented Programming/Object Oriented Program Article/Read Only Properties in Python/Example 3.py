class employee:
    def __init__(self, basesalary, yearsofworking):
        self.basesalary = basesalary
        self.yearsofworking = yearsofworking

    @property
    def salary(self):
        self.salary = 50000


amit = employee(20000, 5)
amit.salary = 10000
print(amit.basesalary, amit.yearsworking, amit.salary)
