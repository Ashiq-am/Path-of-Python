# parent class
class Student:

    # decorator function
    def decor(func):
        def grade(self, marks):
            func(self, marks)
            if marks < 35:
                print('Grade : F')
            elif marks < 50:
                print('Grade : E')
            elif marks < 60:
                print('Grade : D')
            elif marks < 70:
                print('Grade : C')
            elif marks < 80:
                print('Grade : B')
            elif marks < 100:
                print('Grade : A')

        return grade


# child class
class Result(Student):
    @Student.decor
    # instance method
    def result(self, marks):
        print('Your Score : ', marks)


# creating object of parent class
obj = Result()
obj.result(89)
obj.result(34)
