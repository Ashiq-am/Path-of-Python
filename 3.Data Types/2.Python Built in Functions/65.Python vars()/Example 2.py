# Python program to illustrating
# the use of vars() and locals
# when no argument is passed and
# how vars() act as locals().
class Geeks(object):
    def __init__(self):
        self.num1 = 20
        self.num2 = "this is returned"

    def __repr__(self):
        return "Geeks() is returned"

    def loc(self):
        ans = 21
        return locals()

    # Works same as locals()
    def code(self):
        ans = 10
        return vars()

    def prog(self):
        ans = "this is not printed"
        return vars(self)


if __name__ == "__main__":
    obj = Geeks()
    print(obj.loc())
    print(obj.code())
    print(obj.prog())
