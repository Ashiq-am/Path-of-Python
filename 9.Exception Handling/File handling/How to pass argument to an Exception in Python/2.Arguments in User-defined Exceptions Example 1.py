# create user-defined exception
# derived from super class Exception
class MyError(Exception):

    # Constructor or Initializer
    def __init__(self, value):
        self.value = value

    # __str__ is to print() the value
    def __str__(self):
        return (repr(self.value))


try:
    raise (MyError("Some Error Data"))

# Value of Exception is stored in error
except MyError as Argument:
    print('This is the Argument\n', Argument)
