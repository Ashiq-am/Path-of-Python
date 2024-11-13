def foo(a):
    # A new variable is assigned
    # for the new string
    a = "new value"
    print("Inside Function:", a)


# Driver's code
string = "old value"
foo(string)

print("Outside Function:", string)
