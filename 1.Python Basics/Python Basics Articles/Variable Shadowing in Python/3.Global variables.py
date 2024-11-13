# global variable
a = 3


def fn():
    # local variable
    a = 5

    print(a)  # prints 5


    fn()
    print(a)  # prints 3
