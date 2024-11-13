# first parent class
class Person(object):
    def __init__(self, name, idnumber):
        self.name = name
        self.idnumber = idnumber


# second parent class
class Employee(object):
    def __init__(self, salary, post):
        self.salary = salary
        self.post = post


# inheritance from both the parent classes
class Leader(Person, Employee):
    def __init__(self, name, idnumber, salary, post, points):
        self.points = points
        Person.__init__(self, name, idnumber)
        Employee.__init__(self, salary, post)
        print(self.salary)


ins = Leader('Rahul', 882016, 'Assistant Manager', 75000, 560)
