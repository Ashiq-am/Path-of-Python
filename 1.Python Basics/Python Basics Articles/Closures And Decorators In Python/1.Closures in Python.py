# code
def outer_function(msg):
    message = msg

    def inner_function():
        print(message)

    return inner_function


closure = outer_function("Hello, World!")
closure()  # Output: Hello, World!
