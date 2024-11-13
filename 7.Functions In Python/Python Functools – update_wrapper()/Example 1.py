# Defining the decorator
def hi(func):
    def wrapper():
        "Hi has taken over Hello Documentation"
        print("Hi geeks")
        func()

    return wrapper


@hi
def hello():
    "this is the documentation of Hello Function"
    print("Hey Geeks")


# Driver Code
print(hello.__name__)
print(hello.__doc__)
help(hello)
