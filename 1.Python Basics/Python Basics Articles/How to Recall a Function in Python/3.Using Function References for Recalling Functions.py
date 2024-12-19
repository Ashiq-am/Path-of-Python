def greet():
    print("Hello, World!")

def call(func):
    func()

# Recalling the function by passing it as a reference
call(greet)