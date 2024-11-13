def Error_Handler(func):
    def Inner_Function(*args, **kwargs):
        try:
            func(*args, **kwargs)
        except TypeError:
            print(f"{func.__name__} wrong data types. enter numeric")

    return Inner_Function


@Error_Handler
def Mean(a, b):
    print((a + b) / 2)


@Error_Handler
def Square(sq):
    print(sq * sq)


@Error_Handler
def Divide(l, b):
    print(b / l)


Mean(4, 5)
Square(14)
Divide(8, 4)
Square("three")
Divide("two", "one")
Mean("six", "five")
