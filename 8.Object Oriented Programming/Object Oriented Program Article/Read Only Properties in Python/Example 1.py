class student:

    def __init__(self, name, course):
        self.name = name
        self.course = course

    def studentid(self):
        return "student's identification number is \
		{}{}".format(self.name, self.course)


student1 = student("Anita", "MBA")
print(student1.studentid())
