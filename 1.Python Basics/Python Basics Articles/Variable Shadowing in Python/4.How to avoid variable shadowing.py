# global variable
a = 3


def fn():
    global a


# global variable modified
a = 5
print(a)  # prints 5

print(a)  # prints 5
fn()
