class Student:

    def __init__(self, name):
        self.student_name = name

    def __ne__(self, x):
        # return true for different types
        # of object
        if type(x) != type(self):
            return True

        # return True for different values
        if self.student_name != x.student_name:
            return True
        else:
            return False


s1 = Student("Shyam")
s2 = Student("Raju")
s3 = Student("babu rao")

print(s1 != s2)
print(s2 != s3)
