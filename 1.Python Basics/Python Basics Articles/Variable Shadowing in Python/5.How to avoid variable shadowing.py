def outer():
    a = 5


def inner():
    nonlocal a
    a = 3
    print(a)  # prints 3


inner()
print(a)  # prints 3

outer()
